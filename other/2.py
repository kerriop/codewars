# # lambdas
#
# downbytwo = lambda e=5: e - 2
#
# # print(downbytwo(4))
#
# a, b = 1, 2
# y = lambda: a + b
# # print(y())
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # print(list(filter(lambda x: x % 3 == 0, numbers)))
#
# # print(list(map(lambda x: x % 3 == 0, numbers)))
#
# from functools import reduce
#
# print(reduce(lambda x, y: y - x, numbers))
#

def second():
    win_len = 4  # 945747
    k = 1  # 130713
    c1 = k * 2
    c2 = (win_len - k) * 2
    ans = 0
    i = 1
    while ans == 0:
        calced = i * c1 / c2
        if int(calced) == float(calced):
            print(i, (i * c1) / c2)
            ans = 1
        i += 1


def second2(win_len, point):
    left_time = (win_len - point) * 2
    right_time = (0 + point) * 2
    i = 1
    ans = True
    while ans:
        if i * left_time % right_time == 0:
            print(i, i * left_time)
            ans = False
        i += 1


if __name__ == '__main__':
    # second2(4, 1)
    second2(945747, 130713)
