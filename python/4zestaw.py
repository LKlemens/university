#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

# 4.2 ###################################################################### 
print "Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return."

# 3.5 #######################################################
print "zadanie 3.5 Napisać program rysujący miarkę "
userInput = int(raw_input("length of "))
def drawRuler():
    ruler = "".join("|...." for i in range(0, userInput - 1)) + "|"
    defaultNumOfSpaces = 5
    numbers = "".join(str(i) + (defaultNumOfSpaces-len(str(i)))*" "  for i in range(0, userInput))
    return ruler + "\n" + numbers
print drawRuler()

# 3.6 #######################################################
print "zadanie 3.6 Napisać program rysujący prostokąt "

userInput = raw_input("Put height and width ")
def drawRect():
    while True:
        try:
            values = map(int, userInput.split())
            output = ""
            for i in range(0, values[0]):
                output += "".join("+---" for i in range(0, values[1])) + "+" + "\n"
                output += "".join("|   " for i in range(0, values[1])) + "|" + "\n"
            output += "".join("+---" for i in range(0, values[1])) + "+" + "\n"
            break
        except ValueError:
            print "Put only two integer values!"
    return output
print drawRect()


# 4.3 ######################################################################
print "Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię."

factorial = lambda n: n if n == 1 or n == 0 else n * factorial(n-1) # rekurencyjnie
def factorialIter(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact

print factorial(4)
print factorialIter(4)

# 4.4 ######################################################################
print "Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego."

fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)

def fibIter(n):
    if n < 2:
        return n
    fib1 = 0
    fib2 = 1
    for i in range(1, n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


print fib(15)
print fibIter(15)

# 4.5 ######################################################################
print "Napisać funkcję odwracanie(L, left, right), iteracyjnie"
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
print "Napisać funkcję odwracanie(L, left, right), rekurencyjnie"
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
print "Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji"
def sum_recur(sequence):
    sum = 0
    for i in sequence:
        if isinstance(i, (tuple, list)):
            sum += sum_recur(i)
        else:
            sum += i
    return sum

L = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(sum_recur(L))


# 4.7 ###################################################################### 
print "Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji."
def flatten(sequence):
    L = []
    for i in sequence:
        if isinstance(i, (tuple, list)):
            L += flatten(i)
        else:
            L.append(i)
    return L

L = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(L))


