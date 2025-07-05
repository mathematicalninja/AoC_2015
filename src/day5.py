from typing import Generator, Any

from inputFile import inputLines

vowels = ["a", "e", "i", "o", "u"]

# https://adventofcode.com/2015/day/5


def tripleVowel(line: str) -> bool:
    tally = 0
    for vowel in vowels:
        tally = tally + line.count(vowel)
    return tally > 2


def doubleLetter(line: str) -> bool:
    for index in range(len(line) - 1):
        if line[index] == line[index + 1]:
            return True
    return False


pairs = ["ab", "cd", "pq", "xy"]


def naughtyPair(line: str) -> bool:
    for pair in pairs:
        if line.find(pair) != -1:
            return True
    return False


def part1(lines: Generator[str, Any, None]):
    total = 0
    for line in lines:
        if (
            tripleVowel(line)  #
            and doubleLetter(line)
            and not naughtyPair(line)
        ):
            total = total + 1
    return total
    pass


def doubleDouble(line: str):
    for index in range(len(line) - 2):
        pair = line[index : index + 2]
        leftover = line[index + 2 :]
        if leftover.find(pair) != -1:
            return True
    return False


def spaceRepeat(line: str):
    for index in range(len(line) - 2):
        if line[index] == line[index + 2]:
            return True
    return False


def part2(lines: Generator[str, Any, None]):
    total = 0
    for line in lines:
        if doubleDouble(line) and spaceRepeat(line):
            total = total + 1
    return total
    pass


if __name__ == "__main__":
    lines = inputLines(5)
    print("part 1: ", part1(lines))
    lines2 = inputLines(5)
    print("part 2: ", part2(lines2))
    pass
