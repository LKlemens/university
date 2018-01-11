#!/usr/bin/python2.7

import numpy as np

clothes = (
    ("shirt", 75, 7),
    ("jeans", 150, 8),
    ("jumper", 250, 6),
    ("hat", 35, 4),
    ("slips", 10, 3),
    ("shoes", 100, 9),
)


def items_in_bag(amountOfItems, limit, Q):
    nextItemIndex = limit
    table = []
    while nextItemIndex > 0:
        name, weigth = Q[amountOfItems][nextItemIndex]
        table.append(name)
        nextItemIndex = nextItemIndex - weigth
    return table


def dynamic_algorithm(items, limit):
    P = [[0 for i in range(limit + 1)] for j in range(len(items) + 1)]
    Q = [[0 for i in range(limit + 1)] for j in range(len(items) + 1)]

    for item in range(1, len(items) + 1):
        name, itemVal, weigth = items[item - 1]
        for maxWeigth in range(1, limit + 1):
            if maxWeigth >= weigth and P[item -
                                         1][maxWeigth] < P[item][maxWeigth -
                                                                 weigth] + itemVal:
                P[item][maxWeigth] = P[item][maxWeigth - weigth] + itemVal
                Q[item][maxWeigth] = (name, weigth)
            else:
                P[item][maxWeigth] = P[item - 1][maxWeigth]
                Q[item][maxWeigth] = Q[item - 1][maxWeigth]

    print np.matrix(P)

    return items_in_bag(len(items), limit, Q)


print dynamic_algorithm(clothes, 10)
