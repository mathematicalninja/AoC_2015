from icecream import ic
from typing import Generator, Any, Literal, List, Tuple

from inputFile import inputLines
from os.path  import join

from utils.auxFile import makeAuxFile, clearAuxFile, readAuxFile, writeAuxFile

type Pair = List[int]
type mode = Literal["on","off","toggle"]
type Bulbs = List[List[Literal[0,1]]]
type value = Literal[0,1]

def makeBulbs()->Bulbs:
    bulbs = []
    for i in range(1000):
        line = []
        for k in range(1000):
            line.append(0)
        bulbs.append(line)
    return bulbs


def splitThrough(line:str) -> Tuple[str,str,str]:
    """ Splits an input line into [mode, Pair1, Pair2]

    e.g.
    "turn on 0,0 through 999,999"
    ==>[ "on",  "0,0", "999,999"]
    """
    toggleIdx = line.find("toggle")
    if(toggleIdx>=0):
        mode = "toggle"
        newLine = line[7:]
    else:
        # 'turn on 0,0 through 1,1'
        # '____1__2________ugh 1,1'

        space1 = line.find(" ")
        space2 = line.find(" ",space1+1)

        newLine = line[space2+1:]
        mode = line[space1+1:space2]

    throughIdx = newLine.find("through")

    pair1 = newLine[:throughIdx-1]
    pair2 = newLine[throughIdx+8:]
    return (mode,pair1,pair2)

    pass


def parsePair(lineFragment:str)->Pair:
    """ turns string into number Pair: "n,m" -> (n,m)

    e.g.  "0,0" ==> (0,0)

    "999,999" ==> (999,999)

    """

    comma = lineFragment.find(",")
    x = int(lineFragment[:comma])
    y = int(lineFragment[comma+1:])
    return [x,y]

def check_between(n:int,a:int,b:int)->bool:
    if a<=n and n<=b:
        return True
    if b<=n and n<=a:
        return True
    return False


def inRange(currentPair:Pair,firstCorner:Pair,secondCorner:Pair)->bool:
    # note: backwards may be possible e.g. 9,9 -> 3,2
    xCheck = check_between(
        currentPair[0],
        firstCorner[0],
        secondCorner[0]
    )
    yCheck = check_between(
        currentPair[1],
        firstCorner[1],
        secondCorner[1]
    )
    return xCheck and yCheck

def makeRange(pair1:Pair, pair2:Pair) -> Tuple[range, range]:
    return (range(pair1[0], pair2[0]), range(pair1[1], pair2[1]))


def getCoordValue(coord:Pair, lightbulbs: Bulbs) -> value:
    return lightbulbs[coord[0]][coord[1]]

def actOnValue(value:Literal[0,1], action:mode) -> Literal[0,1]:
    match action:
        case "off":
            return 0
        case "on":
            return 1
        case "toggle":
            return 1-value
    pass

def actOnCoord(coord:Pair, action:mode, lightbulbs: Bulbs) -> Bulbs:
    value = getCoordValue(coord, lightbulbs)
    newValue = actOnValue(value,action)
    lightbulbs[coord[0]][coord[1]] = newValue
    return lightbulbs

def actoOnRectangle(corners:Tuple[Pair,Pair], action:mode, lightbulbs: Bulbs) -> Bulbs:
    pass


def parseLine(line:str, lightbulbs: Bulbs) -> Bulbs:
    # turn on 0,0 through 999,999
    # toggle 0,0 through 999,0
    # turn off 499,499 through 500,500
    pass

def auxToBulbs(aux) -> Bulbs:
    pass

def countBulbs(ligthbulbs:Bulbs) -> int:
    pass

def part1(lines: Generator[str, Any, None]):
    # fileName = "day6_part1_Aux.txt"
    # try:
    #     makeAuxFile(fileName)
    #     for i in range(1000):
    #         for k in range(1000):
    #         writeAuxFile(fileName, )
    # except:
    #     clearAuxFile(fileName)
    # finally:
    #     aux = readAuxFile(fileName)
    #     lightbulbs = auxToBulbs(aux)
    lightbulbs= makeBulbs()
    for line in lines:
        lightbulbs = parseLine(line,lightbulbs)
        pass
    return countBulbs(lightbulbs)
    pass

def part2(lines: Generator[str, Any, None]):
    for line in lines:
        pass
    pass


if __name__ == "__main__":
    lines = inputLines(6)
    print("part 1: ", part1(lines))
    lines2 = inputLines(6)
    print("part 2: ", part2(lines2))
    pass