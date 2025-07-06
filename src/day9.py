from icecream import ic
from typing import Generator, Any

from inputFile import inputLines

# https://adventofcode.com/2015/day/9

type singleSteps = dict[str,dict[str,int]] # {start:{end: distance}}

def getCities(line:str)->Tuple[str,str]:
    pass

def getDistance(line:str)->int:
    pass

def addPath(cities:Tuple[str,str], distance:int, steps: singleSteps)->singleSteps:
    pass



def part1(lines: Generator[str, Any, None]):
    # Note that the brute force method will calculate all possible paths which gives n!, with reversible directions this is n!/2.
    # In this case 8!/2 = 20160
    # This is doable

    # Note: to remove half the paths we can just say that the first city in the list if Always visited before the last city.
    # Blah blah combinatorics...trivial.


    cities = set({})

    singleSteps:dict[str,dict[str,int]] = {} # {start:{end: distance}}

    for line in lines:
        CityA, CityB = getCities(line)
        distance = getDistance(line)
        cities.add(CityA)
        cities.add(CityB)
        pass
    pass


def part2(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass


if __name__ == "__main__":
    lines = inputLines(9)
    print("part 1: ", part1(lines))
    lines2 = inputLines(9)
    print("part 2: ", part2(lines2))
    pass
