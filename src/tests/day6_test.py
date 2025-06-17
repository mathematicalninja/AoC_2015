from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputLines_example, inputLines

from src.day6 import part1, part2, getPair, getMode, splitThrough


testCases_part1:List[Tuple[str,int]]=[
    ("turn on 0,0 through 999,999", 1000000),
    ("toggle 0,0 through 999,0", 1000),
    ("turn off 499,499 through 500,500", 0)
]

testCases_part2:List[Tuple[str,int]]=[

]


class Functions(TestCase):
    def setUp(self) -> None:
        self.lightbulbs = [
            [0,1],
            [1,0]
        ]

    def tearDown(self) -> None:
        pass

    def test_splitThrough(self,line:str):
        split = splitThrough("turn on 0,0 through 999,999")

        self.assertEqual(split[1], "turn on")
        self.assertEqual(split[1], "0,0")
        self.assertEqual(split[2], "999,999")
        pass


    def test_getPair(self,lineFragment:str):
        # ->Pair:

        pair1 = getPair("0,0")
        pair2 = getPair("999,999")
        self.assertEqual(pair1, (0,0))
        self.assertEqual(pair2, (999,999))
        pass

    def test_getMode(self,lineFragment:str):
        # -> mode:
        modeOn = getMode("turn on")
        modeOff = getMode("turn off")
        modeToggle = getMode("toggle")

        self.assertEqual(modeOn, "on")
        self.assertEqual(modeToggle, "toggle")
        self.assertEqual(modeOff, "off")
        pass

class Parts(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            self.assertEqual(part1(inputLines_example(case[0])),case[1])
            pass
    def test_part2(self):
        for case in testCases_part2:
            self.assertEqual(part2(inputLines_example(case[0])),case[1])
            pass
class Answers(TestCase):


    def test_answer1(self):
        answerPath = join("answers", "day6.txt")
        inputPath = join("inputFiles", "day6.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open (answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(6)

            self.assertEqual(part1(fullinput),int(answer1.replace("\\n","")))


        else:
            pass

    def test_answer2(self):
        answerPath = join("answers", "day6.txt")
        inputPath = join("inputFiles", "day6.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open (answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(6)

            self.assertEqual(part2(fullinput),int(answer2.replace("\\n","")))


        else:
            pass