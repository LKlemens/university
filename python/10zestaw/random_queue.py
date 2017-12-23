#! /usr/bin/python2.7

from random import randint


class RandomQueue:
    def __init__(self, maxSize):
        self.table = []
        self.maxSize = maxSize

    def push(self, item):
        self.table.append(item)

    def pop(self):
        return self.table.pop(randint(0, len(self.table)) - 1)

    def is_empty(self):
        return len(self.table) == 0

    def is_full(self):
        return len(self.table) == self.maxSize


queue = RandomQueue(10)
for i in range(0, 10):
    queue.push(i)

for i in range(0, 10):
    print queue.pop()
