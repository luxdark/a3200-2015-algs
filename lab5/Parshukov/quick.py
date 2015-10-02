import sys
import random

data = [int(s) for s in sys.stdin.readline().split()]


def part(p, r):
    a = random.randint(p, r)
    x = data[a]
    data[a] = data[r]
    data[r] = x

    count = 0
    for z in range(p, r):
        if data[z] == x:
            y = data[p + count]
            data[p + count] = data[z]
            data[z] = y
            count += 1

    i = p - 1 + count
    for j in range(p + count, r):
        if data[j] < x:
            i += 1
            y = data[j]
            data[j] = data[i]
            data[i] = y

    i += 1
    x = data[i]
    data[i] = data[r]
    data[r] = x

    for z in range(0, count):
        y = data[i - count + z]
        data[i - count + z] = data[z + p]
        data[z + p] = y

    return [i, count]


def quick_sort(p, r):
    if p < r:
        q = part(p, r)
        quick_sort(p, q[0] - q[1])
        quick_sort(q[0] + 1, r)

random.seed()
quick_sort(0, len(data) - 1)
print(data)
