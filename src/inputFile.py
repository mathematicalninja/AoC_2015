from os.path import join
from typing import List


def inputWhole(dayNum: int):
    if dayNum:
        filePath = join("inputFiles", f"day{dayNum}.txt")
        pass
    else:
        filePath = "input.txt"

    with open(filePath, "r") as file:
        r = file.read()

    while True:
        yield r


def inputLines(dayNum: int):
    if dayNum:
        filePath = join("inputFiles", f"day{dayNum}.txt")
        pass
    else:
        filePath = "input.txt"

    with open(filePath, "r") as file:
        fileLines = file.read.splitlines()

    idx = 0
    while idx < len(fileLines):
        # remove trailing newlines
        line = fileLines[idx].replace("\n", "")
        yield line
        idx += 1
    pass


def inputChars(dayNum: int):
    if dayNum:
        filePath = join("inputFiles", f"day{dayNum}.txt")
        pass
    else:
        filePath = "input.txt"

    with open(filePath, "r") as file:
        fileChars = file.read()

    idx = 0
    while idx < len(fileChars):
        yield fileChars[idx]
        idx += 1
    pass


def inputWhole_example(exStr: str):
    return exStr


def inputChar_example(exStr: str):
    idx = 0
    while idx < len(exStr):
        yield exStr[idx]
        idx += 1
    pass


def inputLines_example(exStr: str):
    # remove trailing newlines
    line = exStr.replace("\n", "")
    yield line


def inputMultiLines_example(exStrArr: List[str]):
    idx = 0
    while idx < len(exStrArr):
        yield exStrArr[idx]
        idx += 1
    pass
