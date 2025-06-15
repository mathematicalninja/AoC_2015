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
    total = 0
    for line in lines:
        l, h, w, = lhw(line)
        A = l * h
        B = h * w
        C = w * l

        M = min(A,B,C)

        total += (2*(A+B+C)+M)
    return total

def part2(lines: Generator[str, Any, None]):
    total = 0
    for line in lines:
        l, h, w, = lhw(line)

        # wrap
        wrap = 2*(l+h+w-max(l,h,w))
        # bow
        vol = l*h*w
        total += wrap + vol
    return total


if __name__ == "__main__":
    lines = inputLines(2)
    print("part 1: ", part1(lines))
    lines2 = inputLines(2)
    print("part 2: ", part2(lines2))
    pass