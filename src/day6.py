from icecream import ic
from typing import Generator, Any, Literal, List, Tuple

from inputFile import inputLines
from os.path  import join

from utils.auxFile import makeAuxFile, clearAuxFile, readAuxFile, writeAuxFile

class Pair:
    x:int
    y:int
type mode = Literal["on","off","toggle"]

def makeBulbs()->List[List[Literal[0,1]]]:
    bulbs = []
    for i in range(1000):
        line = []
        for k in range(1000):
            line.append(0)
        bulbs.append(line)
    return bulbs


def splitThrough(line:str) -> Tuple[str,str,str]:
    # "turn on 0,0 through 999,999"
    # ==>[ "turn on",  "0,0", "999,999"]
    pass


def getPair(lineFragment:str)->Pair:
    #  "turn on 0,0" ==> (0,0)
    #  "999,999" ==> (999,999)
    pass

def getMode(lineFragment:str)->mode:
    # turn on ==> Literal['on']
    # toggle  ==> Literal['toggle']
    # turn off  ==> Literal['off']
    pass

def inRange(currentPair:Pair,firstCorner:Pair,secondCorner:Pair)->bool:
    # note: backwards may be possible e.g. 9,9 -> 3,2
    pass

def getCoordValue(coord:Pair, lighbulbs: List[List[Literal[0,1]]])->Literal[0,1]:
    pass

def actOnValue(value:Literal[0,1], action:mode, lighbulbs: List[List[Literal[0,1]]]):
    pass

def actOnCoord(coord:Pair, action:mode):
    value = getCoordValue(coord)
    actOnValue(value,action)
    pass


def parseLine(line:str, lightbulbs: List[List[Literal[0,1]]]) -> List[List[Literal[0,1]]]:
    # turn on 0,0 through 999,999
    # toggle 0,0 through 999,0
    # turn off 499,499 through 500,500
    pass

def auxToBulbs(aux)->List[List[Literal[0,1]]]:
    pass

def countBulbs(ligthbulbs:List[List[Literal[0,1]]])->int:
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