from unittest import TestCase
from os.path import isfile, join

from src.inputFile import inputLines_example, inputLines

from src.day13 import (
    getFirstPerson,
    getFirstSpace,
    getNextSpace,
    getNthSpace,
    getNumber,
    getSecondPerson,
    parseLine,
    part1,
    part2,
    plusOrMinus,
)

testCases_part1: list[tuple[list[str], int]] = [
    (
        [
            "Alice would gain 54 happiness units by sitting next to Bob.",
            "Alice would lose 79 happiness units by sitting next to Carol.",
            "Alice would lose 2 happiness units by sitting next to David.",
            "Bob would gain 83 happiness units by sitting next to Alice.",
            "Bob would lose 7 happiness units by sitting next to Carol.",
            "Bob would lose 63 happiness units by sitting next to David.",
            "Carol would lose 62 happiness units by sitting next to Alice.",
            "Carol would gain 60 happiness units by sitting next to Bob.",
            "Carol would gain 55 happiness units by sitting next to David.",
            "David would gain 46 happiness units by sitting next to Alice.",
            "David would lose 7 happiness units by sitting next to Bob.",
            "David would gain 41 happiness units by sitting next to Carol.",
        ],
        330,
    )
]

testCases_part2: list[tuple[str, int]] = []


class Functions(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getFirstPerson(self) -> None:
        checks = [
            ("Alice would gain 54 happiness units by sitting next to Bob.", "Alice"),
            ("David would gain 46 happiness units by sitting next to Alice.", "David"),
        ]

        for c in checks:
            self.assertEqual(getFirstPerson(c[0]), c[1])
        pass

    def test_getSPerson(self) -> None:
        checks = [
            ("Alice would gain 54 happiness units by sitting next to Bob.", "Bob"),
            ("David would gain 46 happiness units by sitting next to Alice.", "Alice"),
        ]

        for c in checks:
            self.assertEqual(getSecondPerson(c[0]), c[1])
        pass

    def test_getFirstSpace(self) -> None:
        checks: list[tuple[str, int]] = [("Hello World!", 5)]
        for c in checks:
            self.assertEqual(getFirstSpace(c[0]), c[1])
        pass

    def test_getNextSpace(self) -> None:
        checks: list[tuple[str, int, int]] = [
            ("Hello World!", 0, 5),
            ("To be or not to be", 4, 5),
            ("To be or not to be", 9, 12),
        ]
        for c in checks:
            print(c[0])

            self.assertEqual(getNextSpace(c[0], c[1]), c[2])
        pass

    def test_getNthSpace(self) -> None:
        checks: list[tuple[str, int, int]] = [
            ("Hello World!", 1, 5),
            ("To be or not to be", 4, 12),
        ]
        for c in checks:
            print(c[0])

            self.assertEqual(getNthSpace(c[0], c[1]), c[2])
        pass

    def test_getNumber(self) -> None:
        checks: list[tuple[str, int]] = [
            ("Alice would gain 54 happiness units by sitting next to Bob.", 54),
            ("Carol would lose 62 happiness units by sitting next to Alice.", 62),
        ]
        for c in checks:
            self.assertEqual(getNumber(c[0]), c[1])
        pass

    def test_plusOrMinus(self) -> None:
        checks: list[tuple[str, int]] = [
            ("Alice would gain 54 happiness units by sitting next to Bob.", 1),
            ("Carol would lose 62 happiness units by sitting next to Alice.", -1),
        ]
        for c in checks:
            self.assertEqual(plusOrMinus(c[0]), c[1])
        pass

    def test_parseLine(self) -> None:  #
        checks = [
            (
                "Bob would gain 83 happiness units by sitting next to Alice.",
                ("Bob", "Alice", 83),
            ),
            (
                "Bob would lose 7 happiness units by sitting next to Carol.",
                ("Bob", "Carol", -7),
            ),
        ]
        for c in checks:
            self.assertEqual(c[1], parseLine(c[0]))
        pass


class Parts(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            with self.subTest(case=case):
                (self.assertEqual(part1(inputLines_example(case[0])), case[1]))
                pass

    def test_part2(self):
        for case in testCases_part2:
            with self.subTest(case=case):
                self.assertEqual(part2(inputLines_example(case[0])), case[1])
                pass


class Answers(TestCase):
    def test_answer1(self):
        answerPath = join("answers", "day13.txt")
        inputPath = join("inputFiles", "day13.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.read().splitlines()
            fullinput = inputLines(13)

            self.assertEqual(part1(fullinput), int(answer1.replace("\\n", "")))

        else:
            self.assertTrue(False)
            pass

    def test_answer2(self):
        answerPath = join("answers", "day13.txt")
        inputPath = join("inputFiles", "day13.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.read().splitlines()
            fullinput = inputLines(13)

            self.assertEqual(part2(fullinput), int(answer2.replace("\\n", "")))

        else:
            self.assertTrue(False)
            pass
