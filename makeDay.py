from os.path import join
from os import remove as FILE_REMOVE

import fileinput


from typing import Literal, List
import shutil

from selectFromDict import OptionDic, PrintFormat, selectFromDict
from projectSetup import makeInput

type formatTypes = Literal["char", "line", "whole", "multiline"]


def dayFormatter() -> PrintFormat:
    formatter = PrintFormat()
    formatter.className = "Days"

    def initialMessage() -> str:
        return "Choose a day index from: "

    def printLine(option: OptionDic) -> str:  # the line to be printed in the cli
        return f"> Day ({option['internalCode']})"

    def inputLineMessage() -> str:
        return "Day number? "

    def incorrectInputMessage(Raw: str) -> str:
        return f"{Raw} is not recognised."

    def correctInputMessage(option: OptionDic) -> str:
        return f"{option['externalName']} selected."

    formatter.initialMessage = initialMessage
    formatter.printLine = printLine
    formatter.inputLineMessage = inputLineMessage
    formatter.incorrectInputMessage = incorrectInputMessage
    formatter.correctInputMessage = correctInputMessage

    return formatter


def formatFormatter() -> PrintFormat:
    formatter = PrintFormat()
    formatter.className = "fileFormat"

    def initialMessage() -> str:
        return "File formats:"

    def printLine(option: OptionDic) -> str:  # the line to be printed in the cli
        return f"> {option['internalCode']}"

    def inputLineMessage() -> str:
        return "Choose a file format from: "

    def incorrectInputMessage(Raw: str) -> str:
        return f"{Raw} not recognised."

    def correctInputMessage(option: OptionDic) -> str:
        return f"{option['externalName']} selected."

    formatter.initialMessage = initialMessage
    formatter.printLine = printLine
    formatter.inputLineMessage = inputLineMessage
    formatter.incorrectInputMessage = incorrectInputMessage
    formatter.correctInputMessage = correctInputMessage

    return formatter


def chooseDay(num: int) -> int:
    if num > 0:
        return num

    Days: List[OptionDic] = [
        {
            "externalName": f"Day {str(dayNum)}",
            "internalCode": dayNum,
            "externalStub": str(dayNum),
        }
        for dayNum in range(1, 26)
    ]

    selected = selectFromDict(Days, dayFormatter())
    if selected == None:
        raise ValueError()
    typeCast = int(selected["internalCode"])
    return typeCast


def chooseFormat() -> formatTypes:
    formatList: List[formatTypes] = ["char", "line", "whole", "multiline"]
    formats: List[OptionDic] = [
        {
            "externalName": f"Day {str(format)}",
            "internalCode": format,
            "externalStub": format,
            # 'printLine': f"Day {str(dayNum)}",
        }
        for format in formatList
    ]
    selected = selectFromDict(formats, formatFormatter())
    if selected == None:
        raise ValueError()
    return selected["internalCode"]  # type: ignore ==> "internalCode": format,


def makeSrc(dayNum: int, format: formatTypes):
    print(f"Creating `day{dayNum}.py` using `skeleton_{format}.py`...")

    skeleton = join("skeletons", f"skeleton_{format}.py")
    srcFile = join("src", f"day{dayNum}.py")
    try:
        with open(srcFile, "x"):
            pass
        shutil.copy(skeleton, srcFile)
    except:
        print(f"file already exists: '{srcFile}'")
        pass

    try:
        replaceDAYNUMBER(dayNum, srcFile)
    except:
        print("dayNumber replace failed for src")
        return
    removeFile("src", dayNum)


def removeFile(type: Literal["src", "test"], dayNum):
    match type:
        case "src":
            srcPath = join("src", f"day{dayNum}.py.bak")
            FILE_REMOVE(srcPath)
        case "test":
            testPath = join("src", "tests", f"day{dayNum}_test.py.bak")
            FILE_REMOVE(testPath)

    pass


def makeDayExact(dayNum: int, format: formatTypes):
    makeSrc(dayNum, format)
    makeInput(dayNum)
    makeTest(dayNum, format)
    makeBlankAnswer(dayNum)
    print("done")
    pass


def makeDay():
    dayNum = chooseDay(0)
    format = chooseFormat()
    makeDayExact(dayNum, format)
    return


def makeTest(dayNum: int, fileFormat: formatTypes):
    # make f"inputFiles\day{day}.txt" file.
    filePath = join("src", "tests", f"day{dayNum}_test.py")
    print(f"making test: day{dayNum}_test.py")
    try:
        with open(filePath, "x") as file:
            print(f"{filePath} created.")
    except:
        print(f"{filePath} already exists.")
        return
    try:
        skeleton = join("skeletons", f"skeleton_test_{fileFormat}.py")
        shutil.copy(skeleton, filePath)
    except:
        print("skeleton copy failed")
        return

    try:
        replaceDAYNUMBER(dayNum, filePath)
    except:
        print("replaceDAYNUMBER for test failed")
        return
    finally:
        removeFile("test", dayNum)

    pass


def replaceDAYNUMBER(dayNum: int, filePath):
    print(f"{filePath}, {dayNum}")
    with fileinput.FileInput(filePath, inplace=True, backup=".bak") as file:
        for line in file:
            NewLine = line.replace("DAYNUMBER", str(dayNum))
            Uncommeted = NewLine.replace("# ", "")
            print(Uncommeted, end="")


def makeBlankAnswer(dayNum):
    # make f"answers\day{day}.txt" file.
    filePath = join("answers", f"day{dayNum}.txt")
    print(f"making answer file: day{dayNum}.txt")
    try:
        with open(filePath, "x") as file:
            print(f"{filePath} created.")
        with open(filePath, "w") as file:
            file.writelines(["0","0"])
            print(f"Blank answers added.")

    except:
        print(f"{filePath} already exists.")
        return


if __name__ == "__main__":
    makeDay()
    # def R():
    #     return "Nope"
    # f = PrintFormat()
    # f.initialMessage = R
