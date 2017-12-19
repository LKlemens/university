#! /usr/bin/python2.7


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


def print_list(list):
    try:
        temp = list
        print "list printing ..."
        while temp is not None:
            print temp.data
            temp = temp.next
    except ValueError:
        print "list empty"


def remove_head(list):
    try:
        if list.next is None:
            return None, list.data
        temp = list.data
        new_head = list.next
        list.next = None
        list.data = new_head.data
        list.next = new_head.next
        return list, temp
    except (RuntimeError, ValueError, AttributeError):
        print "list empty"


def remove_tail(list):
    try:
        if list.next is None:
            return None, list.data

        temp = list
        while temp.next.next:
            temp = temp.next
        temp.next = None
    except (RuntimeError, ValueError, AttributeError):
        print "list empty"


list = Node(1, Node(2, Node(3)))
print_list(list)
remove_head(list)
print_list(list)
remove_tail(list)
print_list(list)
