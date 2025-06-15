from os.path import join

from typing import Literal, List
import shutil

from selectFromDict import OptionDic, PrintFormat, selectFromDict
from projectSetup import makeInput

type formatTypes = Literal['char', 'line', 'whole']


def dayFormatter()->PrintFormat:
    formatter= PrintFormat()
    formatter.className="Days"

    def initialMessage()->str:
        return "Choose a day index from: "

    def printLine(option:OptionDic)->str: # the line to be printed in the cli
        return f"> Day ({option['internalCode']})"

    def inputLineMessage()->str:
        return "Day number? "

    def incorrectInputMessage(Raw:str)->str:
        return f"{Raw} is not recognised."

    def correctInputMessage(option:OptionDic)-> str:
        return f"{option['externalName']} selected."

    formatter.initialMessage = initialMessage
    formatter.printLine = printLine
    formatter.inputLineMessage = inputLineMessage
    formatter.incorrectInputMessage = incorrectInputMessage
    formatter.correctInputMessage = correctInputMessage

    return formatter

def formatFormatter()-> PrintFormat:
    formatter= PrintFormat()
    formatter.className="fileFormat"

    def initialMessage()->str:
        return "File formats:"

    def printLine(option:OptionDic)->str: # the line to be printed in the cli
        return f"> {option['internalCode']}"

    def inputLineMessage()->str:
        return "Choose a file format from: "

    def incorrectInputMessage(Raw:str)->str:
        return f"{Raw} not recognised."

    def correctInputMessage(option:OptionDic)-> str:
        return f"{option['externalName']} selected."

    formatter.initialMessage = initialMessage
    formatter.printLine = printLine
    formatter.inputLineMessage = inputLineMessage
    formatter.incorrectInputMessage = incorrectInputMessage
    formatter.correctInputMessage = correctInputMessage

    return formatter

def chooseDay(num:int)->str:
    if(num>0):
        return str(num)

    Days:List[OptionDic] = [
        {
            "externalName": f"Day {str(dayNum)}",
            "internalCode": str(dayNum),
            'externalStub': str(dayNum),
        }
        for dayNum in range(1,26)
    ]

    selected  = selectFromDict(Days, dayFormatter())
    if selected == None:
        raise ValueError()
    return selected["internalCode"]


def chooseFormat()->formatTypes:
    formatList:List[formatTypes] = ['char', 'line', 'whole']
    formats:List[OptionDic] = [
        {
            "externalName": f"Day {str(format)}",
            "internalCode": format,
            'externalStub': format,
            # 'printLine': f"Day {str(dayNum)}",
        }
        for format in formatList
    ]
    selected  = selectFromDict(formats, formatFormatter())
    if selected ==None:
        raise ValueError()
    return selected["internalCode"]  # type: ignore ==> "internalCode": format,


def makeSrc(dayNum:str,format:formatTypes):
    print(f"Creating `day{dayNum}.py` using `skeleton_{format}.py`...")

    skeleton = join("skeletons", f"skeleton_{format}.py")
    srcFile = join("src", f"day{dayNum}.py")
    try:
        with open(srcFile, "x"):
            pass
        shutil.copy(skeleton,srcFile)
    except:
        print(f"file already exists: '{srcFile}'")
        pass


def makeDayExact(dayNum:str,format:formatTypes):
    makeSrc(dayNum,format)
    makeInput(dayNum)
    makeTest(dayNum,format)
    print("done")
    pass

def makeDay():
    dayNum = chooseDay(0)
    format = chooseFormat()
    makeDayExact(dayNum,format)
    return


def makeTest(dayNum:str,fileFormat:formatTypes):
    # make f"inputFiles\day{day}.txt" file.
    filePath = join("tests", f"day{dayNum}_test.py")
    print("file",filePath)
    try:
        f = open(filePath, "x")
        print(f"{filePath} created.")
    except:
        print(f"{filePath} already exists.")
        return
    try:
        skeleton = join("skeletons", f"skeleton_test_{fileFormat}.py")
        shutil.copy(skeleton,filePath)
    except:
        print("skeleton copy failed")
    pass



if __name__ == "__main__":
    makeDay()
    # def R():
    #     return "Nope"
    # f = PrintFormat()
    # f.initialMessage = R
