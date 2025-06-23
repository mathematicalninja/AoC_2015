from icecream import ic
from typing import Generator, Any, Tuple, Literal

from inputFile import inputLines


type Signals = dict[str, int]
type Strength = int # Int16
type B = Literal[0,1]

class Int16():
    def __init__(self,n:int) -> None:
        if(n<0):
            self.n = 0
        if(n>2^16-1):
            self.n = 2^16-1
        self.n = n
        pass
    def __str__(self) -> str:
        bs = ""
        for b in reversed(self.bits()):
            bs.join(str(b))
        return bs
        pass
    def bits(self) -> Tuple[B,B,B,B,B,B,B,B,B,B,B,B,B,B,B,B]:
        pass
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