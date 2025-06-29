from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputLines_example, inputLines

from src.day4 import part1, part2

testCases_part1: List[Tuple[str, int]] = [("abcdef", 609043), ("pqrstuv", 1048970)]

testCases_part2: List[Tuple[str, int]] = []


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
        answerPath = join("answers", "day4.txt")
        inputPath = join("inputFiles", "day4.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(4)

            self.assertEqual(part1(fullinput), int(answer1.replace("\\n", "")))

        else:
            pass

    def test_answer2(self):
        answerPath = join("answers", "day4.txt")
        inputPath = join("inputFiles", "day4.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(4)

            self.assertEqual(part2(fullinput), int(answer2.replace("\\n", "")))

        else:
            pass

