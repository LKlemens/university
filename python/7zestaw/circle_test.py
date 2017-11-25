#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest
from math import pi

from circles import Circle


class TestCircles(unittest.TestCase):
    def test_repr_circle(self):
        self.assertEqual(Circle(1, 2, 3).__repr__(), 'Circle(1, 2, 3)')

    def test_str_circle(self):
        self.assertEqual(Circle(1, 2, 3).__str__(), '(1, 2, 3)')

    def test_eq_circle(self):
        self.assertEqual(Circle(1, 2, 3), Circle(1, 2, 3))

    def test_ne_circle(self):
        self.assertNotEqual(Circle(1, 2, 3), Circle(1, 2, 3.1))

    def test_area_circle(self):
        self.assertAlmostEqual(Circle(1, 2, 3).area, 9 * pi)

    def test_move_circle(self):
        foo = Circle(1, 2, 3)
        foo.move(1, 2)
        self.assertEqual(foo, Circle(2, 4, 3))

    def test_cover_circle(self):
        self.assertEqual(
            Circle(2, 2, 1).cover(Circle(4, 4, 1)),
            Circle(3, 3, 3.8284271247461903))


if __name__ == '__main__':
    unittest.main()
