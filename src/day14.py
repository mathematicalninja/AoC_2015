import math
from icecream import ic
from typing import Generator, Any, TypedDict

from src.inputFile import inputLines
from src.utils.spaces import getNthSpace

# https://adventofcode.com/2015/day/14


def calculateLine_part1(speed: int, flightTime: int, restTime: int, raceTime: int):
    cycleTime = flightTime + restTime
    cycles = math.floor(raceTime / cycleTime)
    leftover = raceTime - (cycleTime * cycles)
    if leftover > flightTime:
        leftover = flightTime

    totalFlightTime = flightTime * cycles + leftover

    return totalFlightTime * speed


def parseLine(line: str) -> tuple[int, int, int]:
    speed = int(line[getNthSpace(line, 3) + 1 : getNthSpace(line, 4)])
    flightTime = int(line[getNthSpace(line, 6) + 1 : getNthSpace(line, 7)])
    restTime = int(line[getNthSpace(line, 13) + 1 : getNthSpace(line, 14)])
    return speed, flightTime, restTime


def getName(line: str) -> str:
    space = getNthSpace(line, 1)
    return line[:space]


def part1(lines: Generator[str, Any, None], time: int):
    best = 0
    for line in lines:
        # l = (
        #     "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        # )
        speed, flightTime, restTime = parseLine(line)

        dist = calculateLine_part1(speed, flightTime, restTime, time)
        if dist > best:
            best = dist
    return best


class raindeerDict(TypedDict):
    speed: int
    flightTime: int
    restTime: int
    distance: int
    score: int


def isFlying(raindeerDic: raindeerDict, currentTime: int):
    inFlight = True
    timeTally = 0
    while timeTally < currentTime:
        if inFlight:
            timeTally += raindeerDic["flightTime"]
            if timeTally >= currentTime:
                return True
            inFlight = False
        else:
            timeTally += raindeerDic["restTime"]
            if timeTally >= currentTime:
                return False
            inFlight = True

    pass


def part2(lines: Generator[str, Any, None], time: int):
    data: dict[str, raindeerDict] = {}
    for line in lines:
        name = getName(line)
        speed, flightTime, restTime = parseLine(line)
        data[name] = {  #
            "speed": speed,
            "flightTime": flightTime,
            "restTime": restTime,
            "distance": 0,
            "score": 0,
        }
        pass
    pass
    currentTime = 1
    while currentTime <= time:
        for raindeer in data.keys():
            if isFlying(data[raindeer], currentTime):
                data[raindeer]["distance"] += data[raindeer]["speed"]

        maxDist = max([data[raindeer]["distance"] for raindeer in data.keys()])

        for raindeer in data.keys():
            if data[raindeer]["distance"] == maxDist:
                data[raindeer]["score"] += 1

        currentTime = currentTime + 1
    scores = [data[raindeer]["score"] for raindeer in data.keys()]
    return max(scores)


if __name__ == "__main__":
    lines = inputLines(14)
    print("part 1: ", part1(lines, 2503))
    lines2 = inputLines(14)
    print("part 2: ", part2(lines2, 2503))
    pass
