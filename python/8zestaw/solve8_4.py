#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from math import sqrt
from sys import float_info as fi


def heron(a, b, c):
    """Oblicza pole trojkata za pomoca wzoru Herona."""
    if a < fi.epsilon or b < fi.epsilon or c < fi.epsilon:
        raise ValueError
    if a + b < c or a + c < b or b + c < a:
        raise ValueError

    return sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4


print "Area of triangle a=4,b=5,c=6: " + str(heron(4, 5, 6))
