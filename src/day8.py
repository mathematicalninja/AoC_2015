from icecream import ic
from typing import Generator, Any, Tuple

from inputFile import inputLines

# https://adventofcode.com/2015/day/8


def doubleSlash(line)->Tuple[int,str,int]:
    count = 0
    codeCount = 0
    while True:
        idx = line.find("\\\\")
        if(idx==-1):
            break
        count += 1
        codeCount += 2
        left = line[:idx]
        right = line[idx+2:]
        line = left+right
    return count, line, codeCount


def hexSlash(line)->Tuple[int,str,int]:
    count = 0
    codeCount = 0
    while True:
        idx = line.find("\\x")
        if(idx== -1):
            break
        count += 1
        codeCount += 4
        left = line[:idx]
        right = line[idx+4:]
        line = left+right
    return count, line, codeCount


def quoteSlash(line)->Tuple[int,str,int]:
    count = 0
    codeCount = 0
    while True:
        idx = line.find("\\\"")
        if(idx== -1):
            break
        count += 1
        codeCount += 2
        left = line[:idx]
        right = line[idx+2:]
        line = left+right
    return count, line, codeCount

def encodeSlash(line)->Tuple[int, str]:
    r = ""
    count = 0
    while True:
        idx = line.find("\\")
        if(idx==-1):
            break
        count += 2
        left = line[:idx]
        right = line[idx+1:]
        r = r + left + "\\\\"
        line = right
    return count, r



def countLetters(line:str)->int:
    count = 0
    for i in line:
        if(i.isalnum()):
            count+=1

    return count

def encodeQuote(line)->Tuple[int, str]:
    r = ""
    count = 0
    while True:
        idx = line.find("\"")
        if(idx==-1):
            break
        count += 2
        left = line[:idx]
        right = line[idx+1:]
        r = r + left + "\\\""
        line = right
    return count, r

def parseLine_1(line:str)->int:
    # count_code = len(line) ## BUG: This is wrong
    countSlash_memory, line, countSlash_code  = doubleSlash(line)
    countHex_memory, line, countHex_code= hexSlash(line)
    countQuote_memory,line, countQuote_code= quoteSlash(line)
    count_letters = countLetters(line)
    count = (countHex_memory + countQuote_memory + countSlash_memory)+ count_letters
    count_code = countSlash_code + countHex_code+ countQuote_code+count_letters
    return count_code - count + 2 # +2 for the ""


def parseLine_2(line:str)->int:
    before_line = line
    _ , before_line, countSlash_code  = doubleSlash(before_line)
    _ , before_line, countHex_code= hexSlash(before_line)
    _ ,before_line,  countQuote_code= quoteSlash(before_line)
    count_before_letters = countLetters(before_line)

    count_before = count_before_letters+countSlash_code+countHex_code+countQuote_code

    count_slash, line = encodeSlash(line) # Needs to be before quote
    count_quote, line = encodeQuote(line)
    count_after_letters = countLetters(line)

    count_after = count_slash+count_quote+count_after_letters
    return count_after-count_before

def part1(lines: Generator[str, Any, None]):
    count = 0
    for line in lines:
        count += parseLine_1(line)
    return count
    pass


def part2(lines: Generator[str, Any, None]):
    count = 0
    for line in lines:
        count += parseLine_2(line)
    return count
    pass


if __name__ == "__main__":
    lines = inputLines(8)
    print("part 1: ", part1(lines))
    lines2 = inputLines(8)
    print("part 2: ", part2(lines2))
    pass
