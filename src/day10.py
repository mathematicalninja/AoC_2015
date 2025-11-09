from icecream import ic
from typing import Generator, Any, Tuple

from src.inputFile import inputLines

# https://adventofcode.com/2015/day/10


def grabRepeats(s: str) -> Tuple[str, int, str]:
    if len(s) == 0:
        return ("", 0, "")
    d = s[0]
    count = 1
    while len(s) > 0:
        s = s[1:]
        if s[0] != d:
            break
        count += 1
    return (d, count, s)


def parseLine(line: str) -> str:
    s = line
    r = ""
    count = 0
    while len(s) > 0:
        d, c, s = grabRepeats(s)
        count += c
        r += str(c) + d
    return r


def part1(lines: Generator[str, Any, None]):
    steps = 1  # testing
    # steps = 40 # answer
    for line in lines:
        r = parseLine(line)
        l = len(r)
        lines.append(r)
        if len(lines) >= steps:
            break
    return l
    pass


def part2(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass


if __name__ == "__main__":
    lines = inputLines(10)
    print("part 1: ", part1(lines))
    lines2 = inputLines(10)
    print("part 2: ", part2(lines2))
    pass
