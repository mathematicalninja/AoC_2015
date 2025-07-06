from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputLines_example, inputLines

from src.day8 import part1, part2, doubleSlash, hexSlash,quoteSlash

testCases_part1:List[Tuple[str,int,int]]=[
('""',2, 0),
('"abc"',5,3),
('"aaa\\"aaa"',10,7),
('"\\x27"',6,1),
]

testCases_part2:List[Tuple[str,int]]=[
('""',4),
('"abc"',4),
('"aaa\\"aaa"',6),
('"\\x27"',5),
]


class Functions(TestCase):
    # def setUp(self) -> None:
    #     pass

    # def tearDown(self) -> None:
    #     pass

    def test_doubleSlash(self):
        self.assertEqual(doubleSlash("aa\\\\bb")[0], 1)
        self.assertEqual(doubleSlash("aa\\\\bb")[1], "aabb")

    def test_hexSlash(self):
        self.assertEqual(hexSlash("aa\\x00bb")[0],1)
        self.assertEqual(hexSlash("aa\\x00bb")[1],"aabb")


    def test_quoteSlash(self):
        self.assertEqual(quoteSlash('aa\\"bb')[1],"aabb")
        self.assertEqual(quoteSlash('aa\\"bb')[0],1)

class Parts(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            with self.subTest(case=case):
                p = part1(inputLines_example(case[0]))
                diff = case[1]-case[2]
                self.assertEqual(p,diff)
            pass
    def test_part2(self):
        for case in testCases_part2:
            with self.subTest(case=case):
                self.assertEqual(part2(inputLines_example(case[0])),case[1])
            pass


class Answers(TestCase):
    def test_answer1(self):
        answerPath = join("answers", "day8.txt")
        inputPath = join("inputFiles", "day8.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open (answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(8)

            self.assertEqual(part1(fullinput),int(answer1.replace("\\n","")))


        else:
            pass

    def test_answer2(self):
        answerPath = join("answers", "day8.txt")
        inputPath = join("inputFiles", "day8.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open (answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(8)

            self.assertEqual(part2(fullinput),int(answer2.replace("\\n","")))


        else:
            pass