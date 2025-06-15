

from typing import List, TypedDict


class OptionDic(TypedDict):
    externalStub: str # The Stub to be written before the ")", usually an int.
    externalName: str # The Full name, as displayed to the user
    internalCode: str | int # The **internal** code that will be returned


class PrintFormat():
    className:str
    # template = t"{name} Name" # 3.14 not out yet...

    def initialMessage(self)->str:
        return ""

    def printLine(self, option:OptionDic)->str: # the line to be printed in the cli
        return f"{option['internalCode']}"

    def inputLineMessage(self)->str:
        return ""

    def incorrectInputMessage(self,Raw:str)->str:
        return f"{Raw} not recognised."

    def correctInputMessage(self, option:OptionDic)-> str:
        return f"{option['externalName']} selected."

    pass


def selectFromDict(options:List[OptionDic], formatting: PrintFormat)->OptionDic:
    print(formatting.initialMessage())

    for opt in options:
        print(formatting.printLine(opt))

    inputValid = False
    while not inputValid:
        inputRaw = input(formatting.inputLineMessage())

        for idx in range(len(options)):
            selected = options[idx]
            if inputRaw == str(selected["internalCode"]):
                print(formatting.correctInputMessage(selected))
                return selected
            pass
        print(formatting.incorrectInputMessage(inputRaw))
    return options[0]
