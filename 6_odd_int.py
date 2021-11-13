from collections import Counter


def find_it(seq):
    counter = Counter(seq)
    for key, val in counter.items():
        if val % 2 != 0:
            return key


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))  # 5