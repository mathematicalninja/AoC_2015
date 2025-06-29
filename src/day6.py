from icecream import ic
from typing import Generator, Any, Literal, List, Tuple

from inputFile import inputLines

type Pair = List[int]
type Mode = Literal["on", "off", "toggle"]
type Bulbs = List[List[int]]
type Part = Literal[1, 2]


def makeBulbs() -> Bulbs:
    bulbs = []
    for i in range(1000):
        line = []
        for k in range(1000):
            line.append(0)
        bulbs.append(line)
    return bulbs


def splitThrough(line: str) -> Tuple[Mode, str, str]:
    """Splits an input line into [mode, Pair1, Pair2]

    e.g.
    "turn on 0,0 through 999,999"
    ==>[ "on",  "0,0", "999,999"]
    """
    toggleIdx = line.find("toggle")
    if toggleIdx >= 0:
        mode = "toggle"
        newLine = line[7:]
    else:
        # 'turn on 0,0 through 1,1'
        # '____1__2________ugh 1,1'

        space1 = line.find(" ")
        space2 = line.find(" ", space1 + 1)

        newLine = line[space2 + 1 :]
        mode: Mode = line[space1 + 1 : space2]  # type: ignore

    throughIdx = newLine.find("through")

    pair1 = newLine[: throughIdx - 1]
    pair2 = newLine[throughIdx + 8 :]
    return (mode, pair1, pair2)

    pass


def parsePair(lineFragment: str) -> Pair:
    """turns string into number Pair: "n,m" -> (n,m)

    e.g.  "0,0" ==> (0,0)

    "999,999" ==> (999,999)

    """

    comma = lineFragment.find(",")
    x = int(lineFragment[:comma])
    y = int(lineFragment[comma + 1 :])
    return [x, y]


def check_between(n: int, a: int, b: int) -> bool:
    if a <= n and n <= b:
        return True
    if b <= n and n <= a:
        return True
    return False


def inRange(currentPair: Pair, firstCorner: Pair, secondCorner: Pair) -> bool:
    # note: backwards may be possible e.g. 9,9 -> 3,2
    xCheck = check_between(currentPair[0], firstCorner[0], secondCorner[0])
    yCheck = check_between(currentPair[1], firstCorner[1], secondCorner[1])
    return xCheck and yCheck


def makeRange(pair1: Pair, pair2: Pair) -> Tuple[range, range]:
    x1, y1 = pair1
    x2, y2 = pair2
    return (
        range(min(x1, x2), max(x1, x2) + 1),  #
        range(min(y1, y2), max(y1, y2) + 1),
    )


def getCoordValue(coord: Pair, lightbulbs: Bulbs) -> int:
    return lightbulbs[coord[0]][coord[1]]


def actOnValue(value: int, action: Mode, part: Part) -> int:
    match part:
        case 1:
            match action:
                case "off":
                    return 0
                case "on":
                    return 1
                case "toggle":
                    return 1 - value
        case 2:
            match action:
                case "off":
                    return max(value - 1, 0)
                case "on":
                    return value + 1
                case "toggle":
                    return value + 2
    pass


def actOnCoord(coord: Pair, action: Mode, lightbulbs: Bulbs, part: Part) -> Bulbs:
    value = getCoordValue(coord, lightbulbs)
    newValue = actOnValue(value, action, part)
    lb = lightbulbs
    lb[coord[0]][coord[1]] = newValue
    return lb


def actOnRectangle(
    corners: Tuple[Pair, Pair], action: Mode, lightbulbs: Bulbs, part: Part
) -> Bulbs:
    lb = lightbulbs
    xRange, yRange = makeRange(corners[0], corners[1])
    for x in xRange:
        for y in yRange:
            coord: Pair = [x, y]
            lb = actOnCoord(coord, action, lb, part)
    return lb


def parseLine(line: str, lightbulbs: Bulbs, part: Part) -> Bulbs:
    # turn on 0,0 through 999,999
    # toggle 0,0 through 999,0
    # turn off 499,499 through 500,500
    lineTrio = splitThrough(line)
    action = lineTrio[0]
    corner1 = parsePair(lineTrio[1])
    corner2 = parsePair(lineTrio[2])
    return actOnRectangle((corner1, corner2), action, lightbulbs, part)


def countBulbs(ligthbulbs: Bulbs) -> int:
    xRange = range(len(ligthbulbs))
    yRange = range(len(ligthbulbs[0]))
    count = 0
    for x in xRange:
        for y in yRange:
            count += ligthbulbs[x][y]
    return count


def part1(lines: Generator[str, Any, None]):
    lightbulbs = makeBulbs()
    for line in lines:
        lightbulbs = parseLine(line, lightbulbs, part=1)
        pass
    return countBulbs(lightbulbs)


def part2(lines: Generator[str, Any, None]):
    lightbulbs = makeBulbs()
    for line in lines:
        lightbulbs = parseLine(line, lightbulbs, part=2)
        pass
    return countBulbs(lightbulbs)


if __name__ == "__main__":
    lines = inputLines(6)
    print("part 1: ", part1(lines))
    lines2 = inputLines(6)
    print("part 2: ", part2(lines2))
    pass
