#! /usr/bin/python2.7

import math
import random

__all__ = [
    "random_list", "nearly_sorted_list", "nearly_sorted_list_rev",
    "random_gaussian_list", "random_list_from_set"
]


def random_list(size, maxValue):
    return random.sample(range(0, maxValue), size)


def nearly_sorted_list(size):
    list = []
    for i in range(0, size / 2):
        list.append(2 * i + 1)
    for i in range(0, size / 2):
        list.insert(2 * i + 1, 2 * i)
    return list


def nearly_sorted_list_rev(size):
    list = nearly_sorted_list(size)
    list.reverse()
    return list


def random_gaussian_list(size, mu, mean):
    list = []
    for i in range(0, size):
        list.append(random.gauss(mu, mean))
    return list


def random_list_from_set(size):
    s = set(range(0, size))
    list = []
    for i in range(0, size):
        list.extend(random.sample(s, 1))
    return list


# print nearly_sorted_list(30)
# print nearly_sorted_list_rev(30)
# print random_list(30, 90)
# print random_gaussian_list(30, 12, 5)
# print random_list_from_set(12)
