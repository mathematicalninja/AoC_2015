from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputLines_example, inputLines

from src.day2 import part1, part2

testCases_part1: List[Tuple[str, int]] = [  #
    ("2x3x4", 58),
    ("1x1x10", 43),
]

testCases_part2: List[Tuple[str, int]] = [  #
    ("2x3x4", 34),
    ("1x1x10", 14),
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
        answerPath = join("answers", "day2.txt")
        inputPath = join("inputFiles", "day2.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(2)

            self.assertEqual(part1(fullinput), int(answer1))

        else:  # necessary file doesn't exist.
            self.assertTrue(False)

    def test_answer2(self):
        answerPath = join("answers", "day2.txt")
        inputPath = join("inputFiles", "day2.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(2)

            self.assertEqual(part2(fullinput), int(answer2))

        else:
            self.assertTrue(False)
