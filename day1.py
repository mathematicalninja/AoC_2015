from icecream import ic
from typing import Literal

def day1(part:Literal[1,2]=1):
    left = "("
    right = ")"
    with open("input.txt","r") as inputFile:
        fileText = inputFile.read()
        currentFloor = 0
        index = 1
        for char in fileText:
            if(char == left):
                currentFloor+=1
            if(char == right):
                currentFloor-=1
            if(currentFloor <0 and part==2):
                return index
            index +=1
        return (currentFloor)

if __name__ == "__main__":
    print("part 1: " , day1(1))
    print("part 2: " , day1(2))