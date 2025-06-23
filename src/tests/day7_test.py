from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputMultiLines_example, inputLines

from src.day7 import part1, part2, Signals,getOutputIdentifier, getMode

testCases_part1:List[Tuple[List[str], Signals]]=[
([
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i"
],{
    "d": 72,
    "e": 507,
    "f": 492,
    "g": 114,
    "h": 65412,
    "i": 65079,
    "x": 123,
    "y": 456
})
]

testCases_part2:List[Tuple[List[str], Signals]]=[

]


class Functions(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


    def test_getOuputIdentifier(self):
        self.assertEqual(getOutputIdentifier("123 -> x"),"x")
        self.assertEqual(getOutputIdentifier("p LSHIFT 2 -> q"),"q")

    def test_getMode(self):
        self.assertEqual(getMode("456 -> y"),"INPUT")
        self.assertEqual(getMode("x AND y -> d"),"AND")
        self.assertEqual(getMode("x OR y -> e"),"OR")
        self.assertEqual(getMode("x LSHIFT 2 -> f"),"LSHIFT")
        self.assertEqual(getMode("y RSHIFT 2 -> g"),"RSHIFT")
        self.assertEqual(getMode("NOT x -> h"),"NOT")


class Parts(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            self.assertEqual(part1(inputMultiLines_example(case[0])),case[1])
            pass
    def test_part2(self):
        for case in testCases_part2:
            self.assertEqual(part2(inputMultiLines_example(case[0])),case[1])
            pass

class Answers(TestCase):
    def test_answer1(self):
        answerPath = join("answers", "day7.txt")
        inputPath = join("inputFiles", "day7.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open (answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(7)

            self.assertEqual(part1(fullinput),int(answer1.replace("\\n","")))


        else:
            pass

    def test_answer2(self):
        answerPath = join("answers", "day7.txt")
        inputPath = join("inputFiles", "day7.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open (answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(7)

            self.assertEqual(part2(fullinput),int(answer2.replace("\\n","")))


        else:
            pass