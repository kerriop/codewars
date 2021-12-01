# lambdas

downbytwo = lambda e=5: e - 2

# print(downbytwo(4))

a, b = 1, 2
y = lambda: a + b
# print(y())

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list(filter(lambda x: x % 3 == 0, numbers)))

# print(list(map(lambda x: x % 3 == 0, numbers)))

from functools import reduce

print(reduce(lambda x, y: y - x, numbers))

