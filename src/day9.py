from icecream import ic
from typing import Generator, Any

from inputFile import inputLines

# https://adventofcode.com/2015/day/9


def part1(lines: Generator[str, Any, None]):
    # Note that the brute force method will calculate all possible paths which gives n!, with reversible directions this is n!/2.
    # In this case 8!/2 = 20160
    # This is doable
    for line in lines:
        pass
    pass


def part2(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass


if __name__ == "__main__":
    lines = inputLines(9)
    print("part 1: ", part1(lines))
    lines2 = inputLines(9)
    print("part 2: ", part2(lines2))
    pass
