#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest

from point import Point
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init_rectangle(self):
        point1 = Point(1, 2)
        point2 = Point(3, 4)
        rec = Rectangle(1, 2, 3, 4)
        self.assertEqual(rec.point1, point1)
        self.assertEqual(rec.point2, point2)

    def test_str_rectangle(self):
        self.assertEqual(str(Rectangle(1, 2, 3, 4)), '[(1, 2), (3, 4)]')

    def test_repr_rectangle(self):
        self.assertEqual(repr(Rectangle(1, 2, 3, 4)), 'Rectangle(1, 2, 3, 4)')

    def test_eq_rectangle(self):
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4))

    def test_ne_rectangle(self):
        self.assertNotEqual(Rectangle(1, 2, 3, 4), Rectangle(1, 0, 2, 3))

    def test_center_rectangle(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).center, Point(2, 3))

    def test_area_rectangle(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).area, 4)

    def test_move_rectangle(self):
        foo = Rectangle(1, 2, 3, 4)
        foo.move(1, 1)
        self.assertEqual(foo, Rectangle(2, 3, 4, 5))

    def test_intersection_rectangle(self):
        foo, bar = Rectangle(1, 1, 3, 5), Rectangle(2, 2, 7, 4)
        self.assertEqual(foo.intersection(bar), Rectangle(2, 2, 3, 4))

    def test_cover_rectangle(self):
        foo, bar = Rectangle(1, 1, 3, 5), Rectangle(2, 2, 7, 4)
        self.assertEqual(foo.cover(bar), Rectangle(1, 1, 7, 5))

    def test_make4_rectangle(self):
        foo = Rectangle(1, 1, 5, 5)
        four = foo.make4()
        self.assertEqual(four[0], Rectangle(1, 1, 3, 3))
        self.assertEqual(four[1], Rectangle(3, 3, 5, 5))
        self.assertEqual(four[2], Rectangle(3, 1, 5, 3))
        self.assertEqual(four[3], Rectangle(1, 3, 3, 5))


if __name__ == '__main__':
    unittest.main()
