from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputMultiLines_example, inputLines

from src.day6 import part1, part2, parsePair,  splitThrough, check_between


testCases_part1:List[Tuple[List[str],int]]=[
    (["turn on 0,0 through 999,999"], 1000000),
    (["toggle 0,0 through 999,0"], 1000),
    (["turn off 499,499 through 500,500"], 0),

    (["turn on 0,0 through 999,999","turn off 0,0 through 999,999"], 0),
]

testCases_part2:List[Tuple[List[str],int]]=[


]


class Functions(TestCase):
    def setUp(self) -> None:
        self.lightbulbs = [
            [0,1],
            [1,0]
        ]
        self.strOn = "turn on 0,0 through 1,1"
        self.strOff = "turn off 0,0 through 1,1"
        self.strToggle = "toggle 0,0 through 1,1"

    def tearDown(self) -> None:
        pass


    def test_splitThrough_numbers(self):
        for string in [self.strOn, self.strOff, self.strToggle]:
            with self.subTest(string=string):
                split = splitThrough(string)
                self.assertEqual(split[1], "0,0")
                self.assertEqual(split[2], "1,1")
            pass
        pass

    def test_splitThrough_on(self):
        split = splitThrough(self.strOn)

        self.assertEqual(split[0], "on")
        self.assertEqual(split[1], "0,0")
        self.assertEqual(split[2], "1,1")

    def test_splitThrough_off(self):
        split = splitThrough(self.strOff)

        self.assertEqual(split[0], "off")
        self.assertEqual(split[1], "0,0")
        self.assertEqual(split[2], "1,1")

    def test_splitThrough_toggle(self):
        split = splitThrough(self.strToggle)

        self.assertEqual(split[0], "toggle")
        self.assertEqual(split[1], "0,0")
        self.assertEqual(split[2], "1,1")

    def test_getPair(self):
        # ->Pair:

        pair1 = parsePair("0,0")
        pair2 = parsePair("999,999")
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