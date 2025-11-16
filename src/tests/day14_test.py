from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join

from src.inputFile import inputMultiLines_example, inputLines

from src.day14 import part1, part2

testCases_part1: List[Tuple[List[str], int, int]] = [
    (
        [
            "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        ],
        1000,
        1056,
    ),
    (
        [
            "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
            "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        ],
        1000,
        1120,
    ),
    (
        [
            "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
            "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        ],
        11,
        176,
    ),
    (
        [
            "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
            "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
        ],
        10,
        160,
    ),
]

testCases_part2: List[Tuple[List[str], int, int]] = []


class Functions(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class Parts(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            with self.subTest(case=case):
                self.assertEqual(
                    part1(inputMultiLines_example(case[0]), case[1]), case[2]
                )
                pass

    def test_part2(self):
        for case in testCases_part2:
            with self.subTest(case=case):
                self.assertEqual(part2(inputMultiLines_example(case[0])), case[1])
                pass


class Answers(TestCase):
    def test_answer1(self):
        answerPath = join("answers", "day14.txt")
        inputPath = join("inputFiles", "day14.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.read().splitlines()
            fullinput = inputLines(14)

            self.assertEqual(part1(fullinput, 2503), int(answer1.replace("\\n", "")))

        else:
            self.assertTrue(False)
            pass

    def test_answer2(self):
        answerPath = join("answers", "day14.txt")
        inputPath = join("inputFiles", "day14.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.read().splitlines()
            fullinput = inputLines(14)

            self.assertEqual(part2(fullinput), int(answer2.replace("\\n", "")))

        else:
            self.assertTrue(False)
            pass
