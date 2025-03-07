import random

range_start = 1
range_end = 100
size = 5

random_set = set(random.sample(range(range_start, range_end + 1), size))

print("Random Set:", random_set)
