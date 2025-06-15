def inputFile():
    with open("input.txt","r") as file:
        r = file.read()
    yield r
    raise StopIteration


def inputLines():
    idx = 0
    with open("input.txt","r") as file:
        fileLines = file.readlines()
    while idx < len(fileLines):
         yield fileLines[idx]
         idx+=1
    pass

def inputChars():
    idx = 0
    with open("input.txt","r") as file:
        fileChars = file.read()
    while idx < len(fileChars):
         yield fileChars[idx]
         idx+=1
    pass

def inputFile_example(exStr:str):
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
