import sys
import random

def piff (d):
    d.sort()
    curlen = len (d)
    j = 0
    while j < curlen - 1:
        if d[j] == d[j + 1]:
            curlen -= 1
            for i in range (j, curlen):
                d[i] = d[i + 1]
            j -= 1
        j += 1
    if len (d) > 1:
        d = d[0 : curlen]
    d = [x ** 2 for x in d]

    res = 0
    for x in d:
        l = 0
        r = 0
        while l < len (d):
            if d[l] + d[r] == x:
                res += 1
                l += 1
                r = l
                continue
            if d[l] + d[r] < x:
                if r < len (d) - 1:
                    r += 1
                else:
                    l += 1
                continue
            if d[l] + d[r] > x:
                r -= 1
                l += 1
            if r < l:
                break
    return res

s = "auto"

if s == "console":
    d = [int (s) for s in sys.stdin.readline().split(' ')]
    print (piff(d))

if s == "auto":
    for i in range (1000):
        d = [(x + 1) * (i + 1) + 3 * i * x * x * (i ** 3 + 4)  for x in range (1000)]
        print (d)
        print (piff(d))
