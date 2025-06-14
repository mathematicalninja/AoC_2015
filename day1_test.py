from unittest import TestCase
from typing import List, Tuple

from inputFile import inputChar_example

from day1Redo import part1, part2

testCases_part1:List[Tuple[str,int]] = [
    ("(())",0), ("()()" ,0),
    ("(((",3), ("(()(()(",3),
    ("))(((((",3),
    ("())",-1), ("))(",-1),
    (")))",-3), (")())())",-3),
]

testCases_part2:List[Tuple[str,int]] = [
    (")",1),
    ("()())",5)

]

class Tests(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            self.assertEqual(part1(inputChar_example(case[0])),case[1])
    def test_part2(self):
        for case in testCases_part2:
            self.assertEqual(part2(inputChar_example(case[0])),case[1])