import random


def good_shuffle(list):
    N = len(list)
    for i in range(N-1):
        swap(list, i, random.randrange(i, N))
    return list


def bad_shuffle(list):

    pass


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]


input = list(range(3))
print(good_shuffle(input))


def test_shuffle(func, deck='abc', times=10000):
    input = deck.split()
    for i in range(times):
        output = func(input)

    pass
