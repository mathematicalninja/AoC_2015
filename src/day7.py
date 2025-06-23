from icecream import ic
from typing import Generator, Any, TypedDict

from inputFile import inputLines


class Signals(TypedDict):
    d: int
    e: int
    f: int
    g: int
    h: int
    i: int
    x: int
    y: int

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