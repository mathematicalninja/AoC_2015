from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputLines_example, inputLines

from src.day6 import part1, part2


testCases_part1:List[Tuple[str,int]]=[
    ("turn on 0,0 through 999,999", 1000000),
    ("toggle 0,0 through 999,0", 1000),
    ("turn off 499,499 through 500,500", 0)
]

testCases_part2:List[Tuple[str,int]]=[

]

class Tests(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            self.assertEqual(part1(inputLines_example(case[0])),case[1])
            pass
    def test_part2(self):
        for case in testCases_part2:
            self.assertEqual(part2(inputLines_example(case[0])),case[1])
            pass


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