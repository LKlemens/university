#!/usr/bin/python2
# -*- coding: utf-8 -*-

# 3.1#######################################################
# tutaj są źle wcięcia
# for i in "qwerty": if ord(i) < 100: print i

# poprawione
for i in "qwerty":
    if ord(i) < 100:
        print i

# 3.2#######################################################
# to jest zle poniewaz chcey do dwóch zmiennych przypisać trzy obiekty
# x, y = 1, 2, 2

# nie mozemy operator przypisania nie jest zdefiniowany dla tupli 
# X = 1, 2, 3 ; X[1] = 4

# chcemy przypisać element do pola które jest poza tablicą
# X = [1, 2, 3] ; X[3] = 4

# string nie ma metody append, jesli chcemy cos dodać do stringa, mozemy użyc +
# X = "abc" ; X.append("d")


# pow wymaga przynajmniej dwóch argumentów
# map(pow, range(8))


# 3.3 #######################################################
print "zadanie 3.3 Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3."
for i in range(0, 30):
    if i % 3:
        print i

# 3.4 #######################################################
print "zadanie 3.4  Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x i wypisujący parę x i trzecią potęgę x."

while True:
    try:
        userInput = raw_input("Give a number ")
        if userInput == "stop":
            break
        userInput = int(userInput)
        print [int(userInput), int(userInput), pow(int(userInput), 3)]
    except ValueError:
        print "number, not string!"


# 3.5 #######################################################
print "zadanie 3.5 Napisać program rysujący miarkę "
n = int(raw_input("length of "))
ruler = "".join("|...." for i in range(0, n - 1)) + "|"
defaultNumOfSpaces = 5
numbers = "".join(str(i) + (defaultNumOfSpaces-len(str(i)))*" "  for i in range(0, n))
print ruler + "\n" + numbers

# 3.6 #######################################################
print "zadanie 3.6 Napisać program rysujący prostokąt "

while True:
    try:
        userInput = raw_input("Put height and width ")
        values = map(int, userInput.split())
        for i in range(0, values[0]):
            print "".join("+---" for i in range(0, values[1])) + "+"
            print "".join("|   " for i in range(0, values[1])) + "|"
        print "".join("+---" for i in range(0, values[1])) + "+"

        break
    except ValueError:
        print "Put only two integer values!"

# 3.8 ###################################################################### 
print "zadanie 3.8  Dla dwóch sekwencji znaleźć: (a) listę elementów występujących w obu sekwencjach (bez powtórzeń), (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń)."
a = {1, 2, 3, 4, 4, 4, 5, 6, 7,}
b = { 44, 23, 1, 4, 55, 45, 6, }

a, b = set(a), set(b)
print "a + b without repetition " + str(a.union(b))
print " a+ b common elements " + str(a.intersection(b))

# 3.9 ###################################################################### 
print "zadanie 3.9 Znaleźć listę zawierającą sumy liczb z tych sekwencji. "
print [ sum(i) for i in [[], [4], (1, 2), [3, 4], (5, 6, 7)]  ]

# 3.10 ###################################################################### 
print "zadanie 3.10 Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim "
def roman2int(string):
    result = 0
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} 
    if(len(string) == 1):
        return str( roman[string[0]] )

    guard = 0
    for i in range(0, len(string)):
        if(i < len(string) - 1 and roman[string[i]] < roman[string[i+1]]):
            result += roman[string[i+1]] - roman[string[i]]
            guard += 1
        elif(guard < len(string)):
            result += roman[string[i]]
        guard += 1
    return str( result )

print "M: " + roman2int("M")
print "IX: " + roman2int("IX")
print "XX: " + roman2int("XX")
print "LXX: " + roman2int("LXX")
print "XXXIX: " + roman2int("XXXIX")
