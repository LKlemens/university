#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


class InvalidValueInDenominator:
    pass


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        if y == 0:
            raise InvalidValueInDenominator("Invalid value in denoimnator!")

    def __str__(self):
        return str(self.x / self.y)

    def __repr__(self):
        return self

    def __add__(self, other):
        return Frac(self.x * other.y + other.x * self.y, self.y * other.y)

    def __sub__(self, other):
        return Frac(self.x * other.y - other.x * self.y, self.y * other.y)
        # 1 2, -1 2

    def __mul__(self, other):
        return Frac(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return Frac(self.x * other.y, self.y * other.x)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self.x > 0 and self.y > 0

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __cmp__(self, other):
        sub = self.__sub__(other)
        if sub.x == 0:
            return 0
        return 1 if sub.__pos__() else -1

    def __float__(self):
        return Frac(float(self.x), float(self.y))
