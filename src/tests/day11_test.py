from unittest import TestCase
from typing import List, Tuple
from os.path import isfile, join


from src.inputFile import inputLines_example, inputLines
from src.day11 import (
    hasDoublePair,
    hasNoBadChar,
    hasPair,
    hasStraight,
    incrementPassword,
    isGoodWord,
    isStraight,
    part1,
    part2,
    char,
)

testCases_part1: List[Tuple[str, str]] = [  #
    ("abcdefgh", "abcdffaa"),
    ("ghijklmn", "ghjaabcc"),
]

testCases_part2: List[Tuple[str, int]] = []


class Functions(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_incrementPassword(self):
        examples: list[list[char]] = [
            ["x", "x"],
            ["x", "y"],
            ["x", "z"],
            ["y", "a"],
            ["y", "b"],
        ]
        for i in range(len(examples) - 1):
            self.assertEqual(incrementPassword(examples[i]), examples[i + 1])
        pass

    def test_isStraight(self):
        successes: list[list[char]] = [
            ["a", "b", "c"],
            ["b", "c", "d"],
            ["c", "d", "e"],
            ["x", "y", "z"],
        ]
        fails: list[list[char]] = [
            ["a", "b", "d"],
        ]
        for s in successes:
            self.assertTrue(isStraight(s, 0, 3))
        for f in fails:
            self.assertFalse(isStraight(f, 0, 3))

    def test_hasStraight(self):
        successes: list[list[char]] = [  #
            ["h", "i", "j", "k", "l", "m", "m", "n"],
        ]
        fails: list[list[char]] = [  #
            ["a", "b", "b", "c", "e", "f", "f", "g"],
            ["a", "b", "b", "c", "e", "g", "j", "k"],
        ]

        for s in successes:
            self.assertTrue(hasStraight(s, 3))
        for f in fails:
            self.assertFalse(hasStraight(f, 3))

    def test_hasBadChar(self):
        successes: list[list[char]] = [  #
            ["a", "b", "b", "c", "e", "f", "f", "g"],
            ["a", "b", "b", "c", "e", "g", "j", "k"],
        ]
        fails: list[list[char]] = [  #
            ["h", "i", "j", "k", "l", "m", "m", "n"],
        ]

        for s in successes:
            self.assertTrue(hasNoBadChar(s))
        for f in fails:
            self.assertFalse(hasNoBadChar(f))

    def test_hasPair(self):
        successes: list[list[char]] = [  #
            ["a", "b", "c", "d", "f", "f"],
            ["a", "a"],
            ["a", "b", "b", "c", "e", "f", "f", "g"],
        ]
        fails: list[list[char]] = [  #
            ["h", "i", "j", "k", "l", "m", "n", "o"],
        ]

        for s in successes:
            self.assertTrue(hasPair(s))
        for f in fails:
            self.assertFalse(hasPair(f))

    def test_hasDoublePair(self):
        successes: list[list[char]] = [  #
            ["a", "b", "c", "d", "f", "f", "a", "a"],
            ["a", "b", "b", "c", "e", "f", "f", "g"],
        ]
        fails: list[list[char]] = [  #
            ["h", "i", "j", "k", "l", "m", "m", "n"],
            ["a", "b", "b", "c", "e", "g", "j", "k"],
            ["h", "i", "j", "k", "l", "m", "n", "o"],
        ]

        for s in successes:
            self.assertTrue(hasDoublePair(s))
        for f in fails:
            self.assertFalse(hasDoublePair(f))

    def test_isGoodWord(self):
        successes: list[list[char]] = [  #
            ["a", "b", "c", "d", "f", "f", "a", "a"],
            ["g", "h", "j", "a", "a", "b", "c", "c"],
        ]
        fails: list[list[char]] = [  #
            ["a", "b", "c", "d", "e", "f", "g", "h"],
            ["g", "h", "i", "j", "k", "l", "m", "n"],
            #
            ["h", "i", "j", "k", "l", "m", "m", "n"],
            ["a", "b", "b", "c", "e", "f", "f", "g"],
            #
            ["v", "z", "b", "y", "y", "z", "a", "a"],
        ]

        for s in successes:
            print(s)
            self.assertTrue(isGoodWord(s))
        for f in fails:
            print(f)
            self.assertFalse(isGoodWord(f))


class Parts(TestCase):
    def test_part1(self):
        for case in testCases_part1:
            with self.subTest(case=case):
                self.assertEqual(part1(inputLines_example(case[0])), case[1])
                pass

    def test_part2(self):
        for case in testCases_part2:
            with self.subTest(case=case):
                self.assertEqual(part2(inputLines_example(case[0])), case[1])
                pass


class Answers(TestCase):
    def test_answer1(self):
        answerPath = join("answers", "day11.txt")
        inputPath = join("inputFiles", "day11.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.read().splitlines()
            fullinput = inputLines(11)

            self.assertEqual(part1(fullinput), answer1.replace("\\n", ""))

        else:
            self.assertTrue(False)
            pass

    def test_answer2(self):
        answerPath = join("answers", "day11.txt")
        inputPath = join("inputFiles", "day11.txt")
        if isfile(answerPath) and isfile(inputPath):
            with open(answerPath) as A:
                answer1, answer2 = A.read().splitlines()
            fullinput = inputLines(11)

            self.assertEqual(part2(fullinput), int(answer2.replace("\\n", "")))

        else:
            self.assertTrue(False)
            pass
