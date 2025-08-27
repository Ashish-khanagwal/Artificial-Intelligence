# Example

add = lambda x, y: x + y
print(add(2, 3))


# Example - 2
nums = [1, 2, 3, 4, 5, 6, 7]
squares = list(map(lambda x: x**2, nums))
print(squares)


# Example - 3 (filter())
even_num = list(filter(lambda x: x % 2 == 0, nums))
print(even_num)

# Example -4 (Reduce function)
from functools import reduce

products = reduce(lambda a, b: a * b, nums)
print(products)

sums = reduce(lambda a, b: a + b, nums)
print(sums)
