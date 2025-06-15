from icecream import ic
from typing import Generator, Any

from src.inputFile import inputLines

def lhw(line):
    first = line.find("x")
    second = line[first+1:].find("x")+first

    l = int(line[:first])
    h = int(line[first+1:second+1])
    w = int(line[second+2:])

    return (l, h, w)

def part1(lines: Generator[str, Any, None]):
    for line in inputLines("2"):
        l, h, w, = lhw(line)

    pass

def part2(lines: Generator[str, Any, None]):
    pass


if __name__ == "__main__":
    lines = inputLines("2")
    print("part 1: ", part1(lines))
    lines2 = inputLines("2")
    print("part 2: ", part2(lines2))
    pass