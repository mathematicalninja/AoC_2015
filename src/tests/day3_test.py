from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join


from src.inputFile import inputChar_example, inputChars

from src.day3 import part1, part2

testCases_part1: List[Tuple[str, int]] = []

testCases_part2: List[Tuple[str, int]] = []


class Tests(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            self.assertEqual(part1(inputChar_example(case[0])), case[1])

    def test_part2(self):
        for case in testCases_part2:
            self.assertEqual(part2(inputChar_example(case[0])), case[1])

    def test_answer1(self):
        answerPath = join("answers", "day3.txt")
        inputPath = join("inputFiles", "day3.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputChars(3)

            self.assertEqual(part1(fullinput), int(answer1.replace("\\n", "")))

        else:
            pass

    def test_answer2(self):
        answerPath = join("answers", "day3.txt")
        inputPath = join("inputFiles", "day3.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputChars(3)

            self.assertEqual(part2(fullinput), int(answer2.replace("\\n", "")))

        else:
            pass

