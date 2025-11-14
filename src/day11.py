from icecream import ic
from typing import Generator, Any, Literal, TypeGuard

from src.inputFile import inputLines, inputWhole


# https://adventofcode.com/2015/day/11

# {{{ alphabet

type char = (
    Literal["a"]
    | Literal["b"]
    | Literal["c"]
    | Literal["d"]
    | Literal["e"]
    | Literal["f"]
    | Literal["g"]
    | Literal["h"]
    | Literal["i"]
    | Literal["j"]
    | Literal["k"]
    | Literal["l"]
    | Literal["m"]
    | Literal["n"]
    | Literal["o"]
    | Literal["p"]
    | Literal["q"]
    | Literal["r"]
    | Literal["s"]
    | Literal["t"]
    | Literal["u"]
    | Literal["v"]
    | Literal["w"]
    | Literal["x"]
    | Literal["y"]
    | Literal["z"]
)


def isChar(c: str) -> TypeGuard[char]:
    if c in [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]:
        return True
    return False


alphabet: list[char] = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
# }}}


def nextLetter(char: char) -> char:
    idx = alphabet.index(char)
    if idx == 25:
        return "a"
    return alphabet[idx + 1]


def incrementPassword(word: list[char]) -> list[char]:
    if word[-1] == "z":
        r = incrementPassword(word[:-1])
        r.append("a")
        return r

    r = word[:-1]
    r.append(nextLetter(word[-1]))
    return r


def isStraight(word: list[char], start: int, count: int):
    for i in range(count - 1):
        if nextLetter(word[start + i]) == "a":
            return False
        if nextLetter(word[start + i]) != word[start + i + 1]:
            return False
    return True
    pass


def hasStraight(word: list[char], count: int):
    for i in range(len(word) - count):
        if isStraight(word, i, count):
            return True
    return False


def isBadChar(c: char):
    if c == "i":
        return True
    if c == "o":
        return True
    if c == "l":
        return True
    return False


def hasNoBadChar(word: list[char]):
    for c in word:
        if isBadChar(c):
            return False
    return True


def isPair(word: list[char], idx: int):
    if word[idx] == word[idx + 1]:
        return True
    return False


def hasPair(word: list[char]):
    for i in range(len(word) - 1):
        if isPair(word, i):
            return True
    return False


def hasDoublePair(word: list[char]):
    for i in range(len(word) - 1):
        if hasPair(word[:i]):
            if hasPair(word[i:]):
                return True
    return False


def isGoodWord(word: list[char]) -> bool:
    if not hasNoBadChar(word):
        return False
    if not hasStraight(word, 3):
        return False
    if not hasDoublePair(word):
        return False
    return True


def charList_to_str(chars: list[char]) -> str:
    r = ""
    for c in chars:
        r = r + c
    return r


def strToCharList(word: str) -> list[char]:
    r: list[char] = []
    for c in word:
        if isChar(c):
            r.append(c)
    return r


def getNextPassword(password: str) -> str:
    word = strToCharList(password)

    cap = 26**8
    print(word)
    while cap > 0:
        if isGoodWord(word):
            return charList_to_str(word)
        word = incrementPassword(word)
        cap = cap - 1
    return charList_to_str(word)


def part1(lines: Generator[str, Any, None]) -> str:
    for line in lines:
        nextPassword = getNextPassword(line)
        return nextPassword
        pass


def part2(lines: Generator[str, Any, None]):
    for line in lines:
        first = getNextPassword(line)
        f = strToCharList(first)
        n = incrementPassword(f)
        next = charList_to_str(n)
        return getNextPassword(next)


if __name__ == "__main__":
    line = inputLines(11)
    print("part 1: ", part1(line))
    line2 = inputLines(11)
    print("part 2: ", part2(line2))
    pass
