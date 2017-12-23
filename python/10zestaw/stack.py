#! /usr/bin/python2.7


class Stack:
    def __init__(self, maxSize):
        self.table = []
        self.maxSize = maxSize

    def push(self, num):
        if len(self.table) == self.maxSize:
            raise ValueError
        self.table.append(num)

    def pop(self):
        if len(self.table) == 0:
            raise ValueError
        return self.table.pop()


stack = Stack(2)
stack.push(12)
stack.push(12)
stack.pop()
stack.pop()
