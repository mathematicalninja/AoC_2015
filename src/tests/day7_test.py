from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputLines_example, inputLines

from src.day7 import (
    Wire,
    getEndOfMode,
    getNextInput,
    getSecondInput,
    getTarget,
    parseLineToWire,
    part1,
    part2,
    getFirstInput,
)


type Signals = dict[str, int]

testCases_part1: List[Tuple[List[str], Signals]] = [
    (
        [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i",
        ],
        {
            "d": 72,
            "e": 507,
            "f": 492,
            "g": 114,
            "h": 65412,
            "i": 65079,
            "x": 123,
            "y": 456,
        },
    )
]


testCases_part2: List[Tuple[str, int]] = []


class Functions(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getTargetIdentifier(self) -> None:
        ins = [
            ["123 -> x", "x"],
            ["456 -> y", "y"],
            ["x AND y -> d", "d"],
            ["x OR y -> e", "e"],
            ["x LSHIFT 2 -> f", "f"],
            ["y RSHIFT 2 -> g", "g"],
            ["NOT x -> h", "h"],
            ["NOT y -> i", "i"],
        ]
        for input in ins:
            self.assertEqual(getTarget(input[0]), input[1])

    def test_getNextInput(self) -> None:
        alpha = "abcd efg hijk"
        self.assertEqual(getNextInput(alpha, 8), "hijk")
        self.assertEqual(getNextInput(alpha, 0), "efg")

    def test_getFirstInput(self) -> None:
        ins = [
            ["123 -> x", "123"],
            ["456 -> y", "456"],
            ["x AND y -> d", "x"],
            ["x OR y -> e", "x"],
            ["x LSHIFT 2 -> f", "x"],
            ["y RSHIFT 2 -> g", "y"],
        ]
        for input in ins:
            self.assertEqual(getFirstInput(input[0]), input[1])

    def test_getEndOfMode(self) -> None:
        ins: list[tuple[str, int]] = [
            ("x AND y -> d", 5),
            ("x OR y -> e", 4),
            ("x LSHIFT 2 -> f", 8),
            ("y RSHIFT 2 -> g", 8),
            ("NOT x -> h", 3),
            ("NOT y -> i", 3),
        ]
        for input in ins:
            self.assertEqual(getEndOfMode(input[0]), input[1])

    def test_getSecondInput(self) -> None:
        ins = [
            ["123 -> x", ""],
            ["456 -> y", ""],
            ["x AND y -> d", "y"],
            ["x OR y -> e", "y"],
            ["x LSHIFT 2 -> f", "2"],
            ["y RSHIFT 2 -> g", "2"],
            ["NOT x -> h", "x"],
            ["NOT y -> i", "y"],
        ]
        for input in ins:
            self.assertEqual(getSecondInput(input[0]), input[1])

    def test_parseLine(self) -> None:
        ins: list[tuple[str, Wire]] = [
            ("123 -> x", ("INPUT", "x", "123")),
            ("456 -> y", ("INPUT", "y", "456")),
            ("x AND y -> d", ("AND", "d", "x", "y")),
            ("x OR y -> e", ("OR", "e", "x", "y")),
            ("x LSHIFT 2 -> f", ("LSHIFT", "f", "x", 2)),
            ("y RSHIFT 2 -> g", ("RSHIFT", "g", "y", 2)),
            ("NOT x -> h", ("NOT", "h", "x")),
            ("NOT y -> i", ("NOT", "i", "y")),
        ]
        for input in ins:
            self.assertEqual(parseLineToWire(input[0]), input[1])


class Parts(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            self.assertEqual(part1(inputLines_example(case[0])), case[1])
            pass

    def test_part2(self):
        for case in testCases_part2:
            self.assertEqual(part2(inputLines_example(case[0])), case[1])
            pass


class Answers(TestCase):
    def test_answer1(self):
        answerPath = join("answers", "day7.txt")
        inputPath = join("inputFiles", "day7.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(7)

            self.assertEqual(part1(fullinput), int(answer1.replace("\\n", "")))

        else:
            self.assertTrue(False)

    def test_answer2(self):
        answerPath = join("answers", "day7.txt")
        inputPath = join("inputFiles", "day7.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.readlines()
            fullinput = inputLines(7)

            self.assertEqual(part2(fullinput), int(answer2.replace("\\n", "")))

        else:
            self.assertTrue(False)
