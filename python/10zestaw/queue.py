#! /usr/bin/python2.7


class Queue:
    def __init__(self, maxSize):
        self.table = []
        self.maxSize = maxSize
        self.elements = 0

    def isEmpty(self):
        return self.table == []

    def isFull(self):
        return len(self.table) == self.maxSize

    def push(self, num):
        if self.isFull():
            raise ValueError
        self.table.insert(0, num)
        self.elements += 1

    def pop(self):
        if self.isEmpty():
            raise ValueError
        self.elements -= 1
        return self.table.pop()

    def front(self):
        if self.isEmpty():
            raise ValueError
        return self.table[self.elements - 1]

    def back(self):
        if self.isEmpty():
            raise ValueError
        return self.table[0]
