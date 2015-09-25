import sys
import random

def quick_sort(data):
    if len(data) < 2:
        return data
    left = []
    middle = []
    right = []
    key = data[random.randint(0, len(data) - 1)]
    for i in range(len(data)):
        if data[i] < key:
            left.append(data[i])
        if data[i] > key:
            right.append(data[i])
        if data[i] == key:
            middle.append(data[i])
    return quick_sort(left) + middle + quick_sort(right)

random.seed()
data = [int(s) for s in sys.stdin.readline().split()]

data = quick_sort(data)
print(data)
