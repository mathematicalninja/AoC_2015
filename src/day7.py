from icecream import ic
from typing import Generator, Any, Tuple, Literal, List

from inputFile import inputLines

# https://adventofcode.com/2015/day/7

type Signals = dict[str, int]
type Strength = int  # Int16
type B = Literal[0, 1]
type BitTuple = Tuple[B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B]
"""Note: idx = 0 is 1s, idx = 4 is 16s, etc."""

type Mode = Literal["NOT", "LSHIFT", "RSHIFT", "OR", "AND", "INPUT"]


class Int16:
    def __init__(self, n: int) -> None:
        if n < 0:
            self.n = 0
        if n > 2 ^ 16 - 1:
            self.n = 2 ^ 16 - 1
        self.n = n

    def __str__(self) -> str:
        bs = ""
        for b in reversed(self.bits()):
            bs.join(str(b))
        return bs

    def bits(self) -> BitTuple:
        n = self.n
        bs: List[B] = []
        for i in range(16):
            bs.append(mod2(n))
            n = n // 2
        return tuple(bs)  # type: ignore

    pass


def mod2(n: int) -> B:
    if n % 2:
        return 1
    return 0


def bitsToInt(bits: List[B]) -> int:
    n = 0
    for i in range(16):
        if bits[i]:
            n += bits[i] * 2**i
    return n


def NOT(n: Int16):
    out: List[B] = []
    bits = n.bits()
    for i in range(16):
        out[i] = 1 - bits[i]  # type: ignore
    return Int16(bitsToInt(out))


def LSHIFT(n: Int16, count: int) -> BitTuple:
    excess: List[B] = [0 for i in range(count)]
    bits = list(n.bits())[count:]
    out: List[B] = bits + excess  # Note: this allows for "over-shifting"
    return Int16(bitsToInt(tuple(out[0:16])))  # type: ignore


def RSHIFT(n: Int16, count: int):
    excess: List[B] = [0 for i in range(count)]
    bits = list(n.bits())[:count]
    out: List[B] = excess + bits  # Note: this allows for "over-shifting"
    return Int16(bitsToInt(tuple(out[0:16])))  # type: ignore


def OR(a: Int16, b: Int16):
    aBits = a.bits()
    bBits = b.bits()

    out: List[B] = []
    for i in range(16):
        bit: B = min(aBits[i] + bBits[i], 1)  # type: ignore
        out.append(bit)
    return Int16(bitsToInt(tuple(out[0:16])))  # type: ignore


def AND(a: Int16, b: Int16):
    aBits = a.bits()
    bBits = b.bits()

    out: List[B] = []
    for i in range(16):
        out.append(aBits[i] * bBits[i])  # type: ignore
    return Int16(bitsToInt(tuple(out[0:16])))  # type: ignore


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


def getOutputIdentifier(line: str) -> str:
    idx = line.find("-> ") + 3
    return line[idx:]


def parseLine(line: str, SignalWires: dict):
    sg = SignalWires
    outId = getOutputIdentifier(line)
    mode = getMode(line)

    match mode:
        case "INPUT":
            A = Int16(getInputINPUT(line))
            sg[outId] = A
            pass

        case "NOT":
            B = getInputNot(line)
            value = NOT(B)
            sg[outId] = value

        case "AND":
            A, B = getInputAND(line)
            value = AND(A, B)
            sg[outId] = value

        case "OR":
            A, B = getInputOR(line)
            value = OR(A, B)
            sg[outId] = value

        case "LSHIFT":
            A, B = getInputLSHIFT(line)
            value = LSHIFT(A, B)
            sg[outId] = value

        case "RSHIFT":
            A, B = getInputRSHIFT(line)
            value = RSHIFT(A, B)
            sg[outId] = value
            pass
    pass


def getInputINPUT(line: str) -> int:
    pass


def getInputNot(line: str) -> Int16:
    pass


def getInputAND(line: str) -> Tuple[Int16, Int16]:
    pass


def getInputOR(line: str) -> Tuple[Int16, Int16]:
    pass


def getInputLSHIFT(line: str) -> Tuple[Int16, int]:
    pass


def getInputRSHIFT(line: str) -> Tuple[Int16, int]:
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
