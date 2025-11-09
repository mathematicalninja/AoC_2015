from typing import Literal, Generator, Any
from src.inputFile import inputLines

# https://adventofcode.com/2015/day/7
# https://adventofcode.com/2015/day/7/input


# Idea: change in place text.
# step 1. surround input with (aaa OR bbb) --> ccc
# step 2. reverse order ccc <-- (aaa OR bbb)
# step 3. Table entry {ccc: "(aaa OR bbb)"}
# step 4. 1 million search and replaces. deleting along the way.


## Improvement:
# aaa OR bbb --> ccc
# "values" dic
# {ccc : "(aaa OR bbb)"}
# "inputs" dic
# {aaa: ["ccc"], bbb:["ccc"]}


type input = int | str

type InputWire = tuple[Literal["INPUT"], str, input]
type NotWire = tuple[Literal["NOT"], str, input]

type LshiftWire = tuple[Literal["LSHIFT"], str, input, int]
type RshiftWire = tuple[Literal["RSHIFT"], str, input, int]

type OrWire = tuple[Literal["OR"], str, input, input]
type AndWire = tuple[Literal["AND"], str, input, input]

# Mode, target, input(s?)
type Wire = InputWire | NotWire | LshiftWire | RshiftWire | OrWire | AndWire


type Mode = Literal["INPUT", "NOT", "LSHIFT", "RSHIFT", "OR", "AND"]


def getMode(line: str) -> Mode:
    if line.find("NOT") != -1:
        return "NOT"
    if line.find("LSHIFT") != -1:
        return "LSHIFT"
    if line.find("RSHIFT") != -1:
        return "RSHIFT"
    if line.find("OR") != -1:
        return "OR"
    if line.find("AND") != -1:
        return "AND"
    return "INPUT"


def getEndOfMode(line: str) -> int:
    if line.find("NOT") != -1:
        idx = line.find("NOT")
        return idx + 3
    if line.find("LSHIFT") != -1:
        idx = line.find("LSHIFT")
        return idx + 6
    if line.find("RSHIFT") != -1:
        idx = line.find("RSHIFT")
        return idx + 6
    if line.find("OR") != -1:
        idx = line.find("OR")
        return idx + 2
    if line.find("AND") != -1:
        idx = line.find("AND") + 3
        print(idx, line[idx:])
        return idx
    return 0


u16 = 2**16 - 1  # 65535


def getTarget(line: str) -> str:
    # returns the output wire's string identifier.
    idx = line.find("-> ") + 3
    return line[idx:]


def getFirstInput(line: str) -> str:
    space = line.find(" ")
    return line[:space]


def getNextInput(line: str, index: int) -> str:
    idx2 = line[index:].find(" ") + index + 1
    if line[idx2:].find(" ") == -1:
        idx3 = len(line)
    else:
        idx3 = line[idx2:].find(" ") + idx2
    return line[idx2:idx3]


def getSecondInput(line: str) -> str:
    mode = getMode(line)
    print(line)
    print(mode)
    if mode == "INPUT":
        return ""
    return getNextInput(line, getEndOfMode(line))


def tryInt(inp: input):
    try:
        int(inp)
        return int(inp)
    except:
        return inp


def parseLineToWire(line: str) -> Wire:
    mode = getMode(line)
    target = getTarget(line)

    match mode:
        case "NOT":
            return (  #
                mode,
                getTarget(line),
                tryInt(getSecondInput(line)),
            )
        # "NOT x -> h"
        case "LSHIFT":
            # "x LSHIFT 2 -> f"
            return (  #
                mode,
                target,
                tryInt(getFirstInput(line)),
                int(getSecondInput(line)),
            )
        case "RSHIFT":
            # "y RSHIFT 2 -> g"
            return (  #
                mode,
                target,
                tryInt(getFirstInput(line)),
                int(getSecondInput(line)),
            )
        case "AND":
            # "x AND y -> d"
            return (  #
                mode,
                target,
                tryInt(getFirstInput(line)),
                tryInt(getSecondInput(line)),
            )
        case "OR":
            # "x OR y -> e"
            return (  #
                mode,
                target,
                tryInt(getFirstInput(line)),
                tryInt(getSecondInput(line)),
            )
        case "INPUT":
            # "123 -> x"
            return (  #
                mode,
                target,
                tryInt(getFirstInput(line)),
            )


def isWireCalculable(wire: Wire):
    match wire[0]:
        case "INPUT":
            return True
        case "NOT":
            if type(wire[2]) is int:
                return True
            return False
        case "LSHIFT":
            if type(wire[2]) is int:
                return True
            return False
        case "RSHIFT":
            if type(wire[2]) is int:
                return True
            return False
        case "AND":
            if type(wire[2]) is int and type(wire[3]) is int:
                return True
            return False
        case "OR":
            if type(wire[2]) is int and type(wire[3]) is int:
                return True
            return False
    pass


def getBit(i: int, bit: int):
    modulus = 2**bit
    v = i % modulus
    return v % 2


def bitAnd(inp1: int, inp2: int) -> int:
    value = 0
    for bit in range(16):
        b1 = getBit(inp1, bit)
        b2 = getBit(inp2, bit)
        b = max(0, b1 + b2 - 1) * 2**bit
        value += b
    return value


def bitOr(inp1: int, inp2: int) -> int:
    value = 0
    for bit in range(16):
        b1 = getBit(inp1, bit)
        b2 = getBit(inp2, bit)
        b = min(1, b1 + b2) * 2**bit
        value += b
    return value


def leftShift(inp: int, shift: int):
    value = (inp * 2**shift) // u16
    return value


def rightShift(inp: int, shift: int):
    value = inp // 2**shift
    return value


def calculateWire(wire: Wire) -> InputWire | Literal[False]:
    if not isWireCalculable(wire):
        return False
    match wire[0]:
        case "INPUT":
            return wire
        case "NOT":
            target = wire[1]
            inp = u16 - int(wire[2])
            return ("INPUT", target, inp)
        case "AND":
            target = wire[1]
            inp1 = int(wire[2])
            inp2 = int(wire[3])
            value = bitAnd(inp1, inp2)
            return ("INPUT", target, value)
            pass
        case "OR":
            target = wire[1]
            inp1 = int(wire[2])
            inp2 = int(wire[3])
            value = bitOr(inp1, inp2)
            return ("INPUT", target, value)
            pass
        case "LSHIFT":
            target = wire[1]
            inp1 = int(wire[2])
            inp2 = int(wire[3])
            value = leftShift(inp1, inp2)
            return ("INPUT", target, value)
            pass
        case "RSHIFT":
            target = wire[1]
            inp1 = int(wire[2])
            inp2 = int(wire[3])
            value = rightShift(inp1, inp2)
            return ("INPUT", target, value)
            pass


# TODO:
# 1. Store wires as a dict {target: Wire}
# 2. Loop over key/value pairs in dict
# 3. if calculateWire is False, pass
# 4. else: loop over all wires in dict, replace inputs that match target with the new integer value
#       Delete wire from dict, and store in "calculated" dict.


def ex(wire: Wire):
    mode = wire[0]
    match mode:
        case "INPUT":
            pass
        case "NOT":
            pass
        case "AND":
            pass
        case "OR":
            pass
        case "LSHIFT":
            pass
        case "RSHIFT":
            pass


def part1(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass


def part2(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass


if __name__ == "__main__":
    lines = inputLines(7)
    print("part 1: ", part1(lines))
    lines2 = inputLines(7)
    print("part 2: ", part2(lines2))
    pass
