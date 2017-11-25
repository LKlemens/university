#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from point import Point


class Rectangle(object):
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.point1 = Point(x1, y1)
        self.point2 = Point(x2, y2)

    def __str__(self):
        return '[%s, %s]' % (self.point1, self.point2)

    def __repr__(self):
        return 'Rectangle(%s, %s, %s, %s)' % (self.point1.x, self.point1.y,
                                              self.point2.x, self.point2.y)

    def __eq__(self, other):
        return self.point1 == other.point1 and self.point2 == other.point2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.point1.x + self.point2.x) / 2,
                     (self.point1.y + self.point2.y) / 2)

    def area(self):
        return (self.point2.x - self.point1.x) * (
            self.point2.y - self.point1.y)

    def move(self, x, y):
        self.point1.x += x
        self.point1.y += y
        self.point2.x += x
        self.point2.y += y

    def intersection(self, other):
        return Rectangle(
            max(self.point1.x, other.point1.x),
            max(self.point1.y, other.point1.y),
            min(self.point2.x, other.point2.x),
            min(self.point2.y, other.point2.y))

    def cover(self, other):
        return Rectangle(
            min(self.point1.x, other.point1.x),
            min(self.point1.y, other.point1.y),
            max(self.point2.x, other.point2.x),
            max(self.point2.y, other.point2.y))

    def make4(self):
        middle = self.center
        rect1 = Rectangle(self.point1.x, self.point1.y, middle.x, middle.y)
        rect2 = Rectangle(middle.x, middle.y, self.point2.x, self.point2.y)
        rect3 = Rectangle(middle.x, self.point1.y, self.point2.x, middle.y)
        rect4 = Rectangle(self.point1.x, middle.y, middle.x, self.point2.y)

        return [rect1, rect2, rect3, rect4]
