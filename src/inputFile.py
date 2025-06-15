from typing import Optional

def inputWhole(day:Optional[str]):
    if(day):
        filePath = join("inputFiles", f"{day}.txt")
        pass
    else:
        filePath = "input.txt"

    with open(filePath,"r") as file:
        r = file.read()

    while True:
        yield r


from os.path import join

def inputLines(day:Optional[str]):
    if(day):
        filePath = join("inputFiles", f"{day}.txt")
        pass
    else:
        filePath = "input.txt"

    with open(filePath,"r") as file:
        fileLines = file.readlines()

    idx = 0
    while idx < len(fileLines):
         yield fileLines[idx]
         idx+=1
    pass

def inputChars(day:Optional[str]):
    if(day):
        filePath = join("inputFiles", f"{day}.txt")
        pass
    else:
        filePath = "input.txt"

    with open(filePath,"r") as file:
        fileChars = file.read()

    idx = 0
    while idx < len(fileChars):
         yield fileChars[idx]
         idx+=1
    pass

def inputWhole_example(exStr:str):
    yield exStr
    raise StopIteration



def inputChar_example(exStr:str):
    idx = 0
    while idx < len(exStr):
        yield exStr[idx]
        idx+=1
    pass


def inputLines_example(exStr:str):
    yield exStr
    pass
