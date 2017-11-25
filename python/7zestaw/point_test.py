#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import math
import unittest

from point import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point = Point(1, 2)

    def test_str_point(self):
        self.assertEqual(self.point.__str__(), "(1, 2)")

    def test_repr_point(self):
        self.assertEqual(self.point.__repr__(), "Point(1, 2)")

    def test_eq_poin(self):
        self.assertTrue(self.point.__eq__(Point(1, 2)))
        self.assertFalse(self.point.__eq__(Point(1, 3)))

    def test_ne_poin(self):
        self.assertTrue(self.point.__ne__(Point(1, 3)))
        self.assertFalse(self.point.__ne__(Point(1, 2)))

    def test_add_point(self):
        self.assertEqual(self.point.__add__(Point(2, 2)), Point(3, 4))

    def test_sub_point(self):
        self.assertEqual(self.point.__sub__(Point(1, 4)), Point(0, -2))

    def test_mul_poin(self):
        self.assertEqual(self.point.__mul__(Point(4, 4)), 12)

    def test_corss_point(self):
        self.assertEqual(self.point.cross(Point(4, 4)), -4)

    def test_length_point(self):
        self.assertEqual(self.point.length(), math.sqrt(5))

    def tearDown(self):
        self.point = None


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
