from sys import stdin

__author__ = 'erofeev'

# read ints list from stdin line
coins = [int(i) for i in stdin.readline().split()]

# create 2-d array
x = 10
y = 5
matrix = [[0] * y] * x
print matrix

arr = ['a', 'b']
arr[0], arr[1] = arr[1], arr[0]
