


from unittest import TestCase
from typing import List, Tuple
from inputFile import inputChar_example, inputLines_example

from day4 import part1, part2

testCases_part1:List[Tuple[str,int]]=[
    ("abcdef", 609043),
    ("pqrstuv", 1048970)

]
testCases_part2:List[Tuple[str,int]]=[

]

class Tests(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            self.assertEqual(part1(inputLines_example(case[0])),case[1])
            # self.assertEqual(part1(inputChar_example(case[0])),case[1])
    def test_part2(self):
        for case in testCases_part2:
            self.assertEqual(part2(inputLines_example(case[0])),case[1])
            # self.assertEqual(part2(inputChar_example(case[0])),case[1])