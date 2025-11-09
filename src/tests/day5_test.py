from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputLines_example, inputLines

from src.day5 import part1, part2

testCases_part1: List[Tuple[str, int]] = [
    ("ugknbfddgicrmopn", 1),
    ("jchzalrnumimnmhp", 0),
    ("haegwjzuvuyypxyu", 0),
    ("dvszwmarrgswjxmb", 0),
]

testCases_part2: List[Tuple[str, int]] = [
    ("qjhvhtzxzqqjkmpb", 1),
    ("xxyxx", 1),
    ("aaa", 0),
    ("uurcxstgmygtbstg", 0),
    ("ieodomkazucvgmuy", 0),
]


class Tests(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            self.assertEqual(part1(inputLines_example(case[0])), case[1])
            pass

    def test_part2(self):
        for case in testCases_part2:
            self.assertEqual(part2(inputLines_example(case[0])), case[1])
            pass

    def test_answer1(self):
        answerPath = join("answers", "day5.txt")
        inputPath = join("inputFiles", "day5.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(5)

            self.assertEqual(part1(fullinput), int(answer1.replace("\\n", "")))

        else:
            self.assertTrue(False)

    def test_answer2(self):
        answerPath = join("answers", "day5.txt")
        inputPath = join("inputFiles", "day5.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(5)

            self.assertEqual(part2(fullinput), int(answer2.replace("\\n", "")))

        else:
            self.assertTrue(False)
