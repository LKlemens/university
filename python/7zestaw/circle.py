#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from math import pi, sqrt

from point import Point


class Circle(object):
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError('negative radius')
        self.center = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return 'Circle(%s, %s, %s)' % (self.center.x, self.center.y,
                                       self.radius)

    def __str__(self):
        return '(%s, %s, %s)' % (self.center.x, self.center.y, self.radius)

    def __eq__(self, other):
        return self.center == other.center and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return pi * self.radius * self.radius

    def move(self, x, y):
        self.center.x += x
        self.center.y += y

    def cover(self, other):
        # radius
        x_length = max(self.center.x, other.center.x) - \
            min(self.center.x, other.center.x)
        y_length = max(self.center.y, other.center.y) - \
            min(self.center.y, other.center.y)

        radius = sqrt(x_length * x_length + y_length * y_length) + max(
            self.radius, other.radius)

        x_coordinate = max(self.center.x, other.center.x) - x_length / 2
        y_coordinate = max(self.center.y, other.center.y) - y_length / 2

        return Circle(x_coordinate, y_coordinate, radius)
