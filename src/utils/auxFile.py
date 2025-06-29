from os.path import join


def makeAuxFile(fileName: str):
    filePath = join("inputFiles", fileName)
    with open(filePath, "x"):
        return


def clearAuxFile(fileName: str):
    filePath = join("inputFiles", fileName)
    with open(filePath, "w"):
        return


def readAuxFile(fileName: str):
    filePath = join("inputFiles", fileName)
    with open(filePath, "r") as file:
        return file.read()


def writeAuxFile(fileName: str, text: str):
    filePath = join("inputFiles", fileName)
    with open(filePath, "w") as file:
        file.write(text)
        return

