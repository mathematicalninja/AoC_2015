from os.path import join
from os import write

def makeInput(dayNum:int):
    # make f"inputFiles\day{day}.txt" file.
    filePath = join("inputFiles", f"day{dayNum}.txt")
    print("file",filePath)
    try:
        f = open(filePath, "x")
        print(f"{filePath} created.")
    except:
        print(f"{filePath} already exists.")
    finally:
        return
    pass

if __name__ == "__main__":
    DayList = range(1,26)
    for day in DayList:
        makeInput(day)