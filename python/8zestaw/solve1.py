#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


def solve1(a, b, c):
    if a == 0 and b == 0:
        print("infinity possibilities"
              if c == 0 else "Solution cannot be found; {0} != 0".format(
                  str(c)))
        return

    if a == 0:
        print "x can be any real value, y = {0}".format(str(-c / b))
        return
    if b == 0:
        print "y can be any real value, x = {0}".format(str(-c / a))
        return
    print "x = {0}*y + {1}".format(str(-b / a), str(-c / a))


solve1(12, 5, 6)
solve1(0, 3, 4)
