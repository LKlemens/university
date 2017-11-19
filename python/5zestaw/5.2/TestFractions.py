#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest
import fracs


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.obj = fracs.fractional()

    def test_add_frac(self):
        self.assertEqual(self.obj.add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(self.obj.sub_frac([1, 2], [1, 4]), [2, 8])

    def test_mul_frac(self):
        self.assertEqual(self.obj.mul_frac([1, 2], [1, 4]), [1, 8])

    def test_div_frac(self):
        self.assertEqual(self.obj.div_frac([1, 2], [4, 1]), [1, 8])

    def test_is_positive(self):
        self.assertTrue(self.obj.is_positive([1, 2]))
        self.assertFalse(self.obj.is_positive([-1, 2]))

    def test_is_zero(self):
        self.assertTrue(self.obj.is_zero([0, 2]))
        self.assertFalse(self.obj.is_positive([-1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(self.obj.cmp_frac([0, 2], [0, 2]), 0)
        self.assertEqual(self.obj.cmp_frac([-1, 2], [1, 2]), -1)
        self.assertEqual(self.obj.cmp_frac([1, 2], [1, 3]), 1)

    def test_frac2float(self):
        self.assertTrue(isinstance(self.obj.frac2float([1, 2]), float))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
