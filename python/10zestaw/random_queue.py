#! /usr/bin/python2.7

from random import randrange


class RandomQueue:
    def __init__(self, maxSize):
        self.table = []
        self.maxSize = maxSize

    def push(self, item):
        self.table.append(item)

    def pop(self):
        i = randrange(len(self.table))
        # swap with the last element to awoid deleting from middle of table
        self.table[i], self.table[-1] = self.table[-1], self.table[i]
        return self.table.pop()  # O(1)

    def is_empty(self):
        return len(self.table) == 0

    def is_full(self):
        return len(self.table) == self.maxSize


queue = RandomQueue(10)
for i in range(0, 10):
    queue.push(i)

for i in range(0, 10):
    print queue.pop()
