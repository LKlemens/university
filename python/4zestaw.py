#! /usr/bin/python2.7
# X = "qwerty"
# def func():
#     global X
#     X = "abc"

# func()
# print X
from flatten import *
# 4.3 ######################################################################
factorial = lambda n: n if n == 1 else n * factorial(n-1)
print factorial(4)

# 4.4 ######################################################################
fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
print fib(15)

# 4.5 ######################################################################
L = [5, 4, 3, 2, 1]
def reverseList(List, left, right):
    if abs( right ) > len(List) or abs(left) > len(List):
        raise IndexError
    while left <= right:
        L[left],  L[right] = L[right], L[left]
        left += 1
        right -= 1


reverseList(L, -4, -2)
print L


# 4.5 ###################################################################### 
L = [5, 4, 3, 2, 1]
def reverseListRec(List, left, right):
    if abs( right ) > len(List) or abs(left) > len(List):
        raise IndexError

    L[left],  L[right] = L[right], L[left]
    if left <= right:
        reverseListRec(List, left+1, right-1)

reverseListRec(L, 0, 4)
print L

# 4.6 ###################################################################### 

def sum_recur(sequence):
    sum = 0
    for i in sequence:
        if isinstance(i, (tuple, list)):
            sum += sum_recur(i)
        else:
            sum += i
    return sum

L = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(sum_recur(L))

# 4.7 ###################################################################### 
flatten_lambda = lambda *args: (result for mid in args for result in (flatten(*mid) if isinstance(mid, Iterable) else (mid,)))

L = [[1+2j],(2.,'xd',3),[],[4,"foo",(5,6,7)],8,[9]]
print list(flatten_lambda(L))