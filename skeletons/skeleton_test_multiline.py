from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputMultiLines_example, inputLines

# from src.dayDAYNUMBER import part1, part2

testCases_part1: List[Tuple[List[str], int]] = []

testCases_part2: List[Tuple[List[str], int]] = []


class Functions(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class Parts(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            with self.subTest(case=case):
                # self.assertEqual(part1(inputMultiLines_example(case[0])),case[1])
                pass

    def test_part2(self):
        for case in testCases_part2:
            with self.subTest(case=case):
                # self.assertEqual(part2(inputMultiLines_example(case[0])),case[1])
                pass


class Answers(TestCase):
    def test_answer1(self):
        answerPath = join("answers", "dayDAYNUMBER.txt")
        inputPath = join("inputFiles", "dayDAYNUMBER.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            # fullinput = inputLines(DAYNUMBER)

            # self.assertEqual(part1(fullinput),int(answer1.replace("\\n","")))

        else:
            self.assertTrue(False)
            pass

    def test_answer2(self):
        answerPath = join("answers", "dayDAYNUMBER.txt")
        inputPath = join("inputFiles", "dayDAYNUMBER.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            # fullinput = inputLines(DAYNUMBER)

            # self.assertEqual(part2(fullinput),int(answer2.replace("\\n","")))

        else:
            self.assertTrue(False)
            pass

