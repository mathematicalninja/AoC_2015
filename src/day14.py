import math
from icecream import ic
from typing import Generator, Any

from src.inputFile import inputLines
from src.utils.spaces import getNthSpace

# https://adventofcode.com/2015/day/14


def calculateLine(speed: int, flightTime: int, restTime: int, raceTime: int):
    cycleTime = flightTime + restTime
    cycles = math.floor(raceTime / cycleTime)
    leftover = raceTime - (cycleTime * cycles)
    if leftover > flightTime:
        leftover = flightTime

    totalFlightTime = flightTime * cycles + leftover

    return totalFlightTime * speed


def part1(lines: Generator[str, Any, None], time: int):
    best = 0
    for line in lines:
        # l = (
        #     "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        # )
        speed = int(line[getNthSpace(line, 3) + 1 : getNthSpace(line, 4)])
        flightTime = int(line[getNthSpace(line, 6) + 1 : getNthSpace(line, 7)])
        restTime = int(line[getNthSpace(line, 13) + 1 : getNthSpace(line, 14)])

        dist = calculateLine(speed, flightTime, restTime, time)

        if dist > best:
            best = dist
    return best


def part2(lines: Generator[str, Any, None], time: int):
    for line in lines:
        pass
    pass


if __name__ == "__main__":
    lines = inputLines(14)
    print("part 1: ", part1(lines, 2503))
    lines2 = inputLines(14)
    print("part 2: ", part2(lines2, 2503))
    pass
