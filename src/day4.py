from icecream import ic
import src.inputFile as inputFile
from typing import Generator, Any
from hashlib import md5

# https://adventofcode.com/2015/day/4


def part1(lines: Generator[str, Any, None]):
    i = 0
    for line in lines:
        while i < 2000000:
            concated: str = line + str(i)
            Byted = str.encode(concated)
            hash = md5(Byted).hexdigest()
            hash_str = str(hash)
            r = hash_str.startswith("0" * 5)
            if r:
                return i
            i = i + 1


def part2(lines: Generator[str, Any, None]):
    i = 0
    for line in lines:
        while True:
            concated: str = line + str(i)
            Byted = str.encode(concated)
            hash = md5(Byted).hexdigest()
            hash_str = str(hash)
            r = hash_str.startswith("0" * 6)
            if r:
                print(hash_str, i)
                return i
            i = i + 1


if __name__ == "__main__":
    # chars = inputFile.inputChars()
    # print("part 1: ", part1(chars))
    # chars2 = inputFile.inputChars()
    # print("part 2: ", part2(chars))

    lines = inputFile.inputLines(4)
    print("part 1: ", part1(lines))
    lines2 = inputFile.inputLines(4)
    print("part 2: ", part2(lines2))
    pass
