from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputMultiLines_example, inputLines

from src.day6 import part1
from src.day6 import part2
from src.day6 import parsePair
from src.day6 import splitThrough
from src.day6 import check_between
from src.day6 import getCoordValue
from src.day6 import inRange
from src.day6 import Bulbs
from src.day6 import makeRange
from src.day6 import actOnValue
testCases_part1:List[Tuple[List[str],int]]=[
    (["turn on 0,0 through 999,999"], 1000000),
    (["toggle 0,0 through 999,0"], 1000),
    (["turn off 499,499 through 500,500"], 0),

    (["turn on 0,0 through 999,999","turn off 0,0 through 999,999"], 0),
]

testCases_part2:List[Tuple[List[str],int]]=[


]


class Functions(TestCase):
    def setUp(self) -> None:
        self.lightbulbs: Bulbs = [
            [0,1,0],
            [1,0,1],
            [0,1,0],
        ]
        self.strOn = "turn on 0,0 through 1,1"
        self.strOff = "turn off 0,0 through 1,1"
        self.strToggle = "toggle 0,0 through 1,1"

    def tearDown(self) -> None:
        pass


    def test_splitThrough_numbers(self):
        for string in [self.strOn, self.strOff, self.strToggle]:
            with self.subTest(string=string):
                split = splitThrough(string)
                self.assertEqual(split[1], "0,0")
                self.assertEqual(split[2], "1,1")
            pass
        pass

    def test_splitThrough_on(self):
        split = splitThrough(self.strOn)

        self.assertEqual(split[0], "on")
        self.assertEqual(split[1], "0,0")
        self.assertEqual(split[2], "1,1")

    def test_splitThrough_off(self):
        split = splitThrough(self.strOff)

        self.assertEqual(split[0], "off")
        self.assertEqual(split[1], "0,0")
        self.assertEqual(split[2], "1,1")

    def test_splitThrough_toggle(self):
        split = splitThrough(self.strToggle)

        self.assertEqual(split[0], "toggle")
        self.assertEqual(split[1], "0,0")
        self.assertEqual(split[2], "1,1")

    def test_getPair(self):
        # ->Pair:

        pair1 = parsePair("0,0")
        pair2 = parsePair("999,999")
        self.assertEqual(pair1, [0,0])
        self.assertEqual(pair2, [999,999])

    def test_between(self):
        self.assertTrue(check_between(1,1,1))
        self.assertTrue(check_between(1,0,2))
        self.assertTrue(check_between(1,2,0))
        self.assertTrue(check_between(2,0,2))

        self.assertFalse(check_between(6,1,1))
        self.assertFalse(check_between(6,0,2))
        self.assertFalse(check_between(6,2,0))
        self.assertFalse(check_between(6,0,2))
        pass

    def test_inRange(self):
        z_z = [0,0]
        o_o = [1,1]
        z_o = [0,1]
        o_z = [1,0]
        t_t = [2,2]

        self.assertTrue(inRange(o_o,z_z,t_t))
        self.assertTrue(inRange(o_z,o_z,o_z))
        self.assertTrue(inRange(o_z,o_o,o_z))
        self.assertTrue(inRange(o_o,t_t,z_z)) # Reverse direction


        self.assertFalse(inRange(z_z,t_t,o_o))
        self.assertFalse(inRange(t_t,z_z,z_z))

        pass

    def test_makeRange(self):
        # assert in range...[0,1] in [0,0],[1,1]
        self.assertEqual((range(0,1),range(0,1)), makeRange([0,0],[1,1]))
        # assert in range...[0,1] in [1,1],[0,0]
        self.assertEqual((range(1,0),range(1,0)), makeRange([1,1],[0,0]))
        # assert in range...[1,1] in [1,1],[1,1]
        self.assertEqual((range(1,1),range(1,1)), makeRange([1,1],[1,1]))


        pass

    def test_getCoordValue(self):
        for pair in [[0,0], [1,1]]:
            with self.subTest(pair=pair):
                self.assertEqual(getCoordValue(coord=pair, lightbulbs=self.lightbulbs), 0)

        for pair in [[1,0], [0,1]]:
            with self.subTest(pair=pair):
                self.assertEqual(getCoordValue(coord=pair, lightbulbs=self.lightbulbs), 1)
    pass

    def test_actOnValue(self):
        self.assertEqual(actOnValue(0, "off"), 0)
        self.assertEqual(actOnValue(0, "on"), 1)
        self.assertEqual(actOnValue(0, "toggle"), 1)

        self.assertEqual(actOnValue(1, "off"), 0)
        self.assertEqual(actOnValue(1, "on"), 1)
        self.assertEqual(actOnValue(1, "toggle"), 0)

    def test_actOnCoord(self):

        pass
    def test_actoOnRectangle(self):
        pass
    def test_parseLine(self):
        pass
    def test_auxToBulbs(self):
        pass
    def test_countBulbs(self):
        pass


class Parts(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            self.assertEqual(part1(inputMultiLines_example(case[0])),case[1])
            pass
    def test_part2(self):
        for case in testCases_part2:
            self.assertEqual(part2(inputMultiLines_example(case[0])),case[1])
            pass
class Answers(TestCase):


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