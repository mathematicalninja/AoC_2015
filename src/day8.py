from icecream import ic
from typing import Generator, Any, Tuple

from inputFile import inputLines

# https://adventofcode.com/2015/day/8


def doubleSlash(line)->Tuple[int,str]:
    count = 0
    # print("\\\\")
    while True:
        idx = line.find("\\\\")
        if(idx==-1):
            break
        count += 1
        left = line[:idx]
        right = line[idx+2:]
        line = left+right
    return count, line


def hexSlash(line)->Tuple[int,str]:
    count = 0
    # print("\\\\")
    while True:
        idx = line.find("\\x")
        if(idx== -1):
            break
        count += 1
        left = line[:idx]
        right = line[idx+4:]
        line = left+right
    return count, line





def part1(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass


def part2(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass


if __name__ == "__main__":
    lines = inputLines(8)
    print("part 1: ", part1(lines))
    lines2 = inputLines(8)
    print("part 2: ", part2(lines2))
    pass
