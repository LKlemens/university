#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


def fib(n): return n if n < 2 else fib(n - 1) + fib(n - 2)


def factorial(n): return n if n == 1 or n == 0 else n * factorial(n - 1)
