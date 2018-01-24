#!/usr/bin/python2.7

import numpy as np


def items_in_bag(amountOfItems, limit, Q):
    """Find out which elements was stored.

    Parameters
    ----------
    amountOfItems : int
    limit : int
        Represents max weight able to handle.
    Q : two-dimension array of tuples
        Matrix which store tuple of names and indexes items that was packed.

    Returns
    -------
        list contains names of items

    """
    nextItemIndex = limit
    table = []
    while nextItemIndex > 0:
        name, weigth = Q[amountOfItems][nextItemIndex]
        table.append(name)
        nextItemIndex = nextItemIndex - weigth
    return table


def dynamic_algorithm(items, limit):
    """Calculate optimal proportion of value V and weight W.

    P is a matrix which store max value able to keep.
    Q is a matrix which store names and indexes of items that was packed.

    Parameters
    ----------
    items : list of tuples
        items store tuples consisting of name (string), value (int),
        weight (int)
    limit : int
        represents max weight able to handle

    Returns
    -------
        list of names (string)

    """
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

    # print np.matrix(P)

    return items_in_bag(len(items), limit, Q)
