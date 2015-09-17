__author__ = 'alexkane'

from sys import stdin

first_line = stdin.readline()
n = int(first_line)
second_line = stdin.readline()
m = [int(s) for s in second_line.split(' ')]
counter = 0
index = 0


def calculate(currentIndex, leftover):
    global counter

    if currentIndex == 0:
        if leftover % m[currentIndex] == 0:
            counter += 1
    else:
        div = leftover / m[currentIndex]
        for i in range(0, div + 1):
            newLeftover = leftover
            newLeftover -= i * m[currentIndex]
            if newLeftover == 0:
                counter += 1
            else:
                calculate(currentIndex - 1, newLeftover)


m.sort()

for x in range(m.__len__()):
    if n >= m[x]:
        index = x

calculate(index, n)

print counter
