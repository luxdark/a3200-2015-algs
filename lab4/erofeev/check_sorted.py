# cat norm-random.data | python /Users/erofeev/projects/students/a3200-2015-algs/tmp.py | python /Users/erofeev/projects/students/a3200-2015-algs/lab4/erofeev/check_sorted.py
# cat same-data.data | python /Users/erofeev/projects/students/a3200-2015-algs/tmp.py | python /Users/erofeev/projects/students/a3200-2015-algs/lab4/erofeev/check_sorted.py

from sys import stdin

__author__ = 'erofeev'

line = stdin.readline()
input = [int(s) for s in filter(None, line.split())]

print all(input[i] <= input[i+1] for i in xrange(len(input)-1))