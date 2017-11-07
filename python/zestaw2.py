#! /usr/bin/python2.7
import re

line = "I am trying to sort out a simple list, probably since I cannot identify the type of data I am failing to sort it."

# 2.10
print "2.10     ", len(line.split()), "\n"

# 2.11
print "2.11     ", '_'.join("Hello Word"), "\n"

# 2.12
print "2.12     ", ''.join([word[0] for word in line.split()]), "\n"

# 2.13
print "2.13     ", sum([len(word) for word in line]), "\n"

# 2.14
elem = sorted(line.split(), key=len, reverse=True)[0]
print "2.14     ", elem, len(elem), "\n"

# 2.15
L = [12, 234, 3453, 6542, 345]
print "2.15     ", ''.join(str(L))
print "2.15     ", ''.join([ str(word) for word in L ]), "\n"

# 2.16
Line = "assad;f sadf  GvR dsaf sad"
print "2.16     ", Line.replace('GvR', 'Guido van Rossum'), "\n"

# 2.17
print "2.17     ", sorted(line.split())
print "2.17     ", sorted(line.split(), key=len), "\n"

# 2.18
num = 213491234124012304045489329503205
print "2.18     ", len( re.findall('0', str(num)) ), "\n"

# 2.19
L = [1, 2, 3, 33, 44, 45, 123, 345, 456, 567, 5]
print "2.19     ", ' '.join([str(num).zfill(3) for num in L])
