from icecream import ic
from src.inputFile import inputChars, inputLines
from typing import Generator, Any



def part1(chars: Generator[str, Any, None]):
    currentFloor = 0
    for char in chars:
        if(char == "("):
            currentFloor+=1
        if(char == ")"):
            currentFloor-=1
    return currentFloor

def part2(chars: Generator[str, Any, None]):
    currentFloor = 0
    index = 1
    for char in chars:
        if(char == "("):
            currentFloor+=1
        if(char == ")"):
            currentFloor-=1
        if(currentFloor <0):
            return index
        index +=1
    return currentFloor

    # with open("input.txt","r") as inputFile:
    #     fileText = inputFile.read()
    #     index = 1
    #     for char in fileText:
    #         if(currentFloor <0 and part==2):
    #             return index
    #         index +=1
    #     return (currentFloor)

    pass



if __name__ == "__main__":
    chars = inputChars("1")
    print("part 1: ", part1(chars))
    print("part 2: ", part2(chars))

    # lines = inputLines()
    # print("part 1: ", part1(lines))
    # print("part 2: ", part2(lines))
    pass