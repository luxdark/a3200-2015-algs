from sys import stdin
from random import randint

line = stdin.readline()
input = [int(s) for s in line.split(' ')]


def quick_sort(array, beginning_index, last_index):
    if beginning_index < last_index:
        new_ending_index, new_beginning_index = randomized_partition(array, beginning_index, last_index)
        quick_sort(array, beginning_index, new_ending_index)
        quick_sort(array, new_beginning_index + 1, last_index)


def partition(array, beginning_index, last_index):
    list_of_indexes = []
    default_variable = array[last_index]
    i = beginning_index - 1
    for j in range(beginning_index, last_index):
        if array[j] < default_variable:
            i += 1
            array[i], array[j] = array[j], array[i]
        if array[j] == default_variable:
            i += 1
            array[i], array[j] = array[j], array[i]
            list_of_indexes.append(i)
    array[i + 1], array[last_index] = array[last_index], array[i + 1]
    j = i
    for x in list_of_indexes:
        array[x], array[j] = array[j], array[x]
        j -= 1
    return j, i + 1


def randomized_partition(array, beginning_index, last_index):
    i = randint(beginning_index, last_index)
    array[i], array[last_index] = array[last_index], array[i]
    return partition(array, beginning_index, last_index)


quick_sort(input, 0, len(input) - 1)

for x in input:
    print x,