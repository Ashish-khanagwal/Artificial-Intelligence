from functools import reduce

n = [2, 4, 3, 7, 1, 9]

compare = reduce(lambda a, b: a if a > b else b, n)
print(compare)
