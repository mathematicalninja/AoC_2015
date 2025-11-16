from math import inf
from icecream import ic
from typing import Generator, Any, Literal

from src.inputFile import inputLines
from src.utils.permute import permuteIndices_all

# https://adventofcode.com/2015/day/13


def getFirstPerson(s: str):
    return s[: s.find(" ")]


def getSecondPerson(s: str):
    space_idx: int = len(s) - s[::-1].find(" ")
    return s[space_idx:-1]


def getFirstSpace(s: str) -> int:
    # returns the index of the space itself.
    # e.g. "Hello world!" -> 5
    return s.find(" ")


def getNextSpace(s: str, start: int | None) -> int:
    if start is None:
        start = 0
    f = s[start:].find(" ")
    if f == -1:
        return -1
    return f + start


def getNthSpace(s: str, n: int) -> int:
    if n == 0:
        return -1

    firstSpace = s.find(" ")
    if firstSpace == -1 or n == 1:
        return firstSpace

    idx = firstSpace
    for i in range(1, n):
        idx = getNextSpace(s, idx + 1)
    return idx


def getNumber(s: str) -> int:
    before = getNthSpace(s, 3) + 1
    after = getNthSpace(s, 4)
    return int(s[before:after])


def plusOrMinus(s: str) -> Literal[1] | Literal[-1]:
    if s.find("lose") == -1:
        return 1
    return -1


def parseLine(s: str) -> tuple[str, str, int]:
    name1 = getFirstPerson(s)
    name2 = getSecondPerson(s)
    happiness = plusOrMinus(s) * getNumber(s)
    return (name1, name2, happiness)


def addValueToData(
    name1: str, name2: str, happiness: int, dataStruct: dict[str, dict[str, int]]
):
    if name1 not in dataStruct.keys():
        dataStruct[name1] = {}
    if name2 not in dataStruct[name1].keys():
        dataStruct[name1][name2] = happiness
    else:
        dataStruct[name1][name2] += happiness

    if name2 not in dataStruct.keys():
        dataStruct[name2] = {}
    if name1 not in dataStruct[name2].keys():
        dataStruct[name2][name1] = happiness
    else:
        dataStruct[name2][name1] += happiness


def part1(lines: Generator[str, Any, None]):
    dataLines: list[tuple[str, str, int]] = []
    for line in lines:
        dataLines.append(parseLine(line))
    pass

    firstNames = [datum[0] for datum in dataLines]
    secondNames = [datum[1] for datum in dataLines]
    nameSet = set(firstNames + secondNames)

    dataStruct: dict[str, dict[str, int]] = {}

    for line in dataLines:
        name1 = line[0]
        name2 = line[1]
        happiness = line[2]
        addValueToData(name1, name2, happiness, dataStruct)
    pass

    names: list[str] = []
    for name in nameSet:
        names.append(name)
    pass

    count = len(nameSet)
    permutations = permuteIndices_all(count)

    best = -inf
    for perm in permutations:
        total = 0

        nameOrder = [names[idx] for idx in perm]
        for seat in range(count):
            # seat 0 is next to seat -1
            prev = seat - 1
            name1 = nameOrder[prev]
            name2 = nameOrder[seat]
            total += dataStruct[name1][name2]
        pass
        if total > best:
            best = total
    pass
    return best


def part2(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass


if __name__ == "__main__":
    lines = inputLines(13)
    print("part 1: ", part1(lines))
    lines2 = inputLines(13)
    print("part 2: ", part2(lines2))
    pass
