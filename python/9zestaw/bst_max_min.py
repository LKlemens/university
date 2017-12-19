#! /usr/bin/python2.7


class node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return "{}".format(str(self.value))


def bst_max(top):
    if top is None:
        raise ValueError
    while top.right:
        top = top.right
    return top.value


def bst_min(top):
    if top is None:
        raise ValueError
    while top.left:
        top = top.left
    return top.value


top = node(7, node(5, node(1), node(10)), node(33, node(21, 29)))
print(bst_min(top))
print(bst_max(top))
