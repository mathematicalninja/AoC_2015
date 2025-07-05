from icecream import ic
import inputFile as inputFile
from typing import Generator, Any
from hashlib import md5

# https://adventofcode.com/2015/day/4


def part1(lines: Generator[str, Any, None]):
    i = 1
    for line in lines:
        while i < 2000000:
            i = i + 1
            concated: str = line + str(i)
            Byted = str.encode(concated)
            hash = md5(Byted).hexdigest()
            # print(line + str(i))
            hash_str = str(hash)
            r = hash_str.startswith("00000")
            if r:
                return i


def part2(lines: Generator[str, Any, None]):
    i = 1
    for line in lines:
        while True:
            i = i + 1
            concated: str = line + str(i)
            Byted = str.encode(concated)
            hash = md5(Byted).hexdigest()
            # print(line + str(i))
            hash_str = str(hash)
            r = hash_str.startswith("000000")
            if r:
                print(hash_str, i)
                return i


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
