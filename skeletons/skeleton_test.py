from unittest import TestCase
from typing import List, Tuple
from src.inputFile import inputChar_example, inputLines_example

# from src.dayDAYNUMBER import part1, part2

##  https://adventofcode.com/2015/day/DAYNUMBER

testCases_part1: List[Tuple[str, int]] = []

testCases_part2: List[Tuple[str, int]] = []


class Tests(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            with self.subTest(case=case):
                # self.assertEqual(part1(inputLines_example(case[0])),case[1])
                # self.assertEqual(part1(inputChar_example(case[0])),case[1])
                pass

    def test_part2(self):
        for case in testCases_part2:
            with self.subTest(case=case):
                # self.assertEqual(part2(inputLines_example(case[0])),case[1])
                # self.assertEqual(part2(inputChar_example(case[0])),case[1])
                pass
