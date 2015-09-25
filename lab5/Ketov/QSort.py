from sys import stdin

first_line = stdin.readline()
massiv = [int(s) for s in first_line.split()]

nachalo = 0
konec = len(massiv) - 1


def swap(a, i, j):
    c = a[i]
    a[i] = a[j]
    a[j] = c


def qsort(a, l, r):
    l = nachalo
    r = konec
    seredina = len(a) / 2
    print (a[seredina])
    while l <= r:
        while (a[l] < a[seredina]) and (l <= konec):
            l += 1
        while (a[r] > a[seredina]) and (r >= nachalo):
            r -= 1
        if l <= r:
            swap(a, l, r)
            l += 1
            r -= 1
    print (a)

    if r > nachalo:
        qsort(a, nachalo, r)
    if l < konec:
        qsort(a, l, konec)


qsort(massiv, nachalo, konec)
print (massiv)
