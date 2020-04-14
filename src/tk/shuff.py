import random


def shuff(n=10):
    arr = list(range(n))
    random.shuffle(arr)
    return arr


# print(shuff())
