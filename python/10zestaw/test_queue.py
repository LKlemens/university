#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(4)

    def test_push_pop(self):
        self.queue.push(1)
        self.queue.push(2)
        self.queue.push(3)
        self.assertEqual(1, self.queue.front())
        self.assertEqual(3, self.queue.back())
        self.assertEqual(1, self.queue.pop())
        self.assertEqual(2, self.queue.pop())
        self.assertEqual(3, self.queue.pop())

    def test_pop_raise(self):
        with self.assertRaises(ValueError):
            self.queue.pop()

    def test_push_raise(self):
        self.queue.push(12)
        self.queue.push(12)
        self.queue.push(12)
        self.queue.push(12)
        with self.assertRaises(ValueError):
            self.queue.push(12)


if __name__ == '__main__':
    unittest.main()
