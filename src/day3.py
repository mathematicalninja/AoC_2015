from icecream import ic
from typing import Literal, Generator, Any
from inputFile import inputChars


def gift(x: int, y: int, Logs: dict[int, dict[int, int]], total: int):
    try:
        X = Logs[x]
    except KeyError:
        Logs[x] = {y: 0}
        total += 1
    finally:
        X = Logs[x]

    try:
        Y = X[y]
    except KeyError:
        X[y] = 0
        total += 1
    finally:
        Y = X[y]
    Logs[x][y] += 1
    return (Logs, total)


def move(
    char: Literal[
        ">",
        "<",
        "^",
        "v",
    ],
):
    match char:
        case ">":
            return (1, 0)
        case "<":
            return (-1, 0)
        case "^":
            return (0, 1)
        case "v":
            return (0, -1)


def part1(chars: Generator[str, Any, None]):
    Logs = {}
    total = 0

    # initial present
    x = 0
    y = 0
    Logs, total = gift(x, y, Logs, total)

    for char in chars:
        dx, dy = move(char)  # type: ignore -- File contains correct characters.
        x, y = x + dx, y + dy
        Logs, total = gift(x, y, Logs, total)
    return total


def part2(chars: Generator[str, Any, None]):
    Logs = {}
    total = 0

    x = 0
    y = 0

    Robo_x = 0
    Robo_y = 0

    Logs, total = gift(x, y, Logs, total)
    Logs, total = gift(Robo_x, Robo_y, Logs, total)

    santa: bool = True

    for char in chars:
        dx, dy = move(char)  # type: ignore -- File contains correct characters.
        if santa:
            x, y = x + dx, y + dy
            Logs, total = gift(x, y, Logs, total)
            santa = not santa
        else:
            Robo_x, Robo_y = Robo_x + dx, Robo_y + dy

            Logs, total = gift(Robo_x, Robo_y, Logs, total)
            santa = not santa

    return total


if __name__ == "__main__":
    chars1 = inputChars(3)
    print("part 1: ", part1(chars1))
    chars2 = inputChars(3)
    print("part 2: ", part2(chars2))

