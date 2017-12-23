#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import unittest

from stack import Stack


class TestStac(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(2)

    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(2, self.stack.pop())
        self.assertEqual(1, self.stack.pop())

    def test_pop_raise(self):
        with self.assertRaises(ValueError):
            self.stack.pop()

    def test_push_raise(self):
        self.stack.push(12)
        self.stack.push(12)
        with self.assertRaises(ValueError):
            self.stack.push(12)


if __name__ == '__main__':
    unittest.main()
