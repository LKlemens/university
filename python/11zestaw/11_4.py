#! /usr/bin/python2.7

import sys
from time import clock

import generateList


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


def benchmarks(list):
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(list) + 50))
    print ""
    print "Times check for {}".format(len(list))

    start = clock()
    mergeSort(list)
    end = clock()
    print "merge sort time {}".format(end - start)

    start = clock()
    bubbleSort(list)
    end = clock()
    print "bubble sort time {}".format(end - start)

    start = clock()
    quickSort(list)
    end = clock()
    print "quick sort time {}".format(end - start)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print alist

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print alist

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print alist

benchmarks(generateList.random_list(100, 100))
benchmarks(generateList.random_list(1000, 1000))
benchmarks(generateList.random_list(1000, 1000))
benchmarks(generateList.random_list(10000, 10000))
benchmarks(generateList.random_list(100000, 100000))
benchmarks(generateList.random_list(1000000, 1000000))

#  Spośród wybranych algorytmów najszybszym jest merge sort

# Times check for 100
# merge sort time 0.000555
# bubble sort time 0.00081
# quick sort time 0.000999

# Times check for 1000
# merge sort time 0.007803
# bubble sort time 0.081168
# quick sort time 0.079636

# Times check for 1000
# merge sort time 0.007491
# bubble sort time 0.08112
# quick sort time 0.077676

# Times check for 10000
# merge sort time 0.096068
# bubble sort time 8.56279
# quick sort time 7.605907

# Times check for 100000
# merge sort time 1.263396
# bubble sort time 1030.953011
# quick sort time 893.679811
