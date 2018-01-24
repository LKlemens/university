#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest

from knapsack_problem import dynamic_algorithm

clothes = (
    ("shirt", 75, 7),
    ("jeans", 150, 8),
    ("jumper", 250, 6),
    ("hat", 35, 4),
    ("slips", 10, 3),
    ("shoes", 100, 9),
)


class TestKnapsack(unittest.TestCase):
    def test_output(self):
        table = dynamic_algorithm(clothes, 10)
        self.assertEqual(table[0], 'hat')
        self.assertEqual(table[1], 'jumper')


if __name__ == '__main__':
    unittest.main()
