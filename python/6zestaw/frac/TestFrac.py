#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest

from Frac import Frac


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.frac1 = Frac(1, 2)

    def test_add_frac(self):
        self.assertEqual(self.frac1.__add__(Frac(1, 3)), Frac(5, 6))

    def test_sub_frac(self):
        self.assertEqual(self.frac1.__sub__(Frac(1, 4)), Frac(2, 8))

    def test_mul_frac(self):
        self.assertEqual(self.frac1.__mul__(Frac(1, 4)), Frac(1, 8))

    def test_div_frac(self):
        self.assertEqual(self.frac1.__div__(Frac(4, 1)), Frac(1, 8))

    def test_is_positive(self):
        self.assertTrue(self.frac1.__pos__())
        self.assertFalse(Frac(-1, 2).__pos__())

    def test_cmp_frac(self):
        self.assertEqual(self.frac1.__cmp__(Frac(1, 2)), 0)
        self.assertEqual(self.frac1.__cmp__(Frac(1, -2)), -1)
        self.assertEqual(self.frac1.__cmp__(Frac(1, 3)), 1)

    def test_frac2float(self):
        self.assertTrue(isinstance(self.frac1.__float__().x, float))
        self.assertTrue(isinstance(self.frac1.__float__().y, float))

    def tearDown(self):
        self.frac1 = None


if __name__ == '__main__':
    unittest.main()
