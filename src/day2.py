from icecream import ic
from typing import Literal, List

from src.inputFile import inputLines

def lhw():
     for line in inputLines():
        first = line.find("x")
        second = line[first+1:].find("x")+first
        l = int(line[:first])
        h = int(line[first+1:second+1])
        w = int(line[second+2:])

        yield (l, h, w)



def part1():
    total = 0
    for l,h,w in lhw():
        A = l * h
        B = h * w
        C = w * l

        M = min(A,B,C)

        total += (2*(A+B+C)+M)
    return total


def part2():
    total = 0
    for l,h,w in lhw():
        # wrap
        wrap = 2*(l+h+w-max(l,h,w))
        # bow
        vol = l*h*w
        total += wrap + vol
    return total






if __name__ == "__main__":
    print("part 1: " , part1())
    print("part 2: " , part2())