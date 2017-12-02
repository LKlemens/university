#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from random import uniform


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.

    n oznacza liczbę losowanych punktów.

    """
    radius = 10.0
    hits = 0

    for i in range(n):
        x, y = uniform(0, 2 * radius), uniform(0, 2 * radius)

        if ((x - radius)**2 + (y - radius)**2 < radius**2):
            hits += 1

    return 4.0 * hits / n


print "Iterations 10, Approximately Pi = {0}".format(str(calc_pi(10)))
print "Iterations 100, Approximately Pi = {0}".format(str(calc_pi(100)))
print "Iterations 1000, Approximately Pi = {0}".format(str(calc_pi(1000)))
print "Iterations 10000, Approximately Pi = {0}".format(str(calc_pi(10000)))
print "Iterations 100000, Approximately Pi = {0}".format(str(calc_pi(100000)))
