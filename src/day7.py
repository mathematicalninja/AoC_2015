from icecream import ic
from typing import Generator, Any, Tuple, Literal, List

from inputFile import inputLines


type Signals = dict[str, int]
type Strength = int # Int16
type B = Literal[0,1]
type BitTuple = Tuple[B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]
"""Note: idx = 0 is 1s, idx = 4 is 16s, etc."""

class Int16():
    def __init__(self,n:int) -> None:
        if(n<0):
            self.n = 0
        if(n>2^16-1):
            self.n = 2^16-1
        self.n = n

    def __str__(self) -> str:
        bs = ""
        for b in reversed(self.bits()):
            bs.join(str(b))
        return bs

    def bits(self) -> BitTuple:
        n = self.n
        bs:List[B] = []
        for i in range(16):
            bs.append(mod2(n))
            n = n//2
        return tuple(bs) # type: ignore
    pass

def mod2(n:int)->B:
    if n%2:
        return 1
    return 0

def bitsToInt(bits: BitTuple)->int:
    n=0
    for i in range(16):
        if bits[i]:
            n += bits[i]*2**i
    return n

    pass

def NOT(n:Int16):
    pass

def LSHIFT(n:Int16,count:int):
    pass

def RSHIFT(n:Int16,count:int):
    pass

def OR(a:Int16,b:Int16):
    pass

def AND(a:Int16,b:Int16):
    pass

def part1(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass

def part2(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass


if __name__ == "__main__":
    lines = inputLines(7)
    print("part 1: ", part1(lines))
    lines2 = inputLines(7)
    print("part 2: ", part2(lines2))
    pass