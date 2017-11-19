#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import unittest
import polys

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x*x
        self.obj = polys.Polys()

    def test_add_poly(self):
        self.assertEqual(self.obj.add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self):
        self.assertEqual(self.obj.sub_poly(self.p1, self.p2), [0, 1, -1])

    def test_mul_poly(self):
        self.assertEqual(self.obj.mul_poly(self.p1, self.p2), [1])

    def test_is_zero(self):
        self.assertTrue(self.obj.is_zero([0,0,0]))
        self.assertFalse(self.obj.is_zero([0,1,0]))

    def test_cmp_poly(self): pass

    def test_eval_poly(self): pass

    def test_combine_poly(self): pass

    def test_pow_poly(self): pass

    def test_diff_poly(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

