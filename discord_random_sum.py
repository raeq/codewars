"""
How to divide the number 53 by 3 random numbers with the sum of 53
"""
import itertools
import random


def random_triplets(target: int):
    t1 = random.choice([x for x in itertools.combinations(range(1, target), 3) if sum(x) == target])
    return t1, target / t1[0], target / t1[1], target / t1[2]


print(random_triplets(80))
