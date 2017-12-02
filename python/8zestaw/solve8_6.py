#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from time import clock


def P_rec(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif j == 0:
        return 0
    elif i == 0:
        return 1
    elif i > 0 and j > 0:
        return 0.5 * (P_rec(i - 1, j) + P_rec(i, j - 1))


def P_dynamic(i, j):
    value = P_dynamic.dictionary.get((i, j))
    if value:
        return value
    elif j == 0:
        return 0
    elif i == 0:
        return 1
    elif i > 0 and j > 0:
        value = 0.5 * (P_dynamic(i - 1, j) + P_dynamic(i, j - 1))
        P_dynamic.dictionary[(i, j)] = value
        return value


P_dynamic.dictionary = {(0, 0): 0.5, (1, 0): 0, (0, 1): 1}


def test(i, j):
    start = clock()
    P_rec(i, j)
    middle = clock()
    P_dynamic(i, j)
    stop = clock()

    return (middle - start, stop - middle)


print "Values: {0}, {1}".format(10, 12)
foo = test(10, 20)
print "Recursive " + repr(foo[0])
print "Dynamic " + repr(foo[1])
