# for i in range(5, 10, 1):
#     print(i)
#
# print('--------------------')

# def my_range(n, start=0, step=1):
#     i = start
#     while i < n:
#         yield i
#         i += step
#
def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    while stop > start:
        yield start
        start += step


for i in my_range(10):
    print(i)


#
#
# # for x in my_range(5):
# #     print(x)
#
# yo = my_range(3)
#
# print(yo.__next__())
# print(yo.close())
#


def my_decorator(input_arg):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f'{input_arg}\n{result}\n{input_arg}'

        return wrapper

    return the_real_decorator


# gen_1 = (x for x in range(5))
# gen_2 = (x for x in range(5, 10))
#
#
# def generator():
#     yield from gen_1
#     yield from gen_2
#
#
# gen = generator()
#
# result = [n for n in gen]
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(result)


def subgenerator():
    yield 'World'


def generator():
    yield 'Hello'
    yield from subgenerator()  # Запрашиваем значение из субгенератора
    yield '!'


#
# for i in generator():
#     print(i, end=' ')
# Вывод
# Hello World !

# d = {'a': 1, 'b': {'c': 2}} -> Iterable[('a', 1), ('b.c': 2)]
# d = {'key1': 'value1', 'key2': {'subkey2': 'subvalue2'}}
#
#
# def coroutine(f):
#     def wrap(*args, **kwargs):
#         gen = f(*args, **kwargs)
#         gen.send(None)
#         return gen
#
#     return wrap
#
#
# @coroutine
# def calc():
#     while True:
#         x, y = yield
#         result = x + y
#         print(result)
#
#
# c = calc()
# c.send((1, 3))  # 4


# def BinarySearch(lys, val):
#     first = 0
#     last = len(lys) - 1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first + last) // 2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val < lys[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return index

# print(BinarySearch([10, 20, 30, 40, 50], 20))

# dic = {'rating': 4.666666666666667}

#  d = {'a': 1, 'b': {'c': 2}} -> Iterable[('a', 1), ('b.c': 2)]

# d = {'a': 1, 'b': {'c': 2}}
#
#
# def something(a):
#     ret = []
#     for e in a:
#         if ...:
#             ret.append(e)
#         else:
#             something(e)
#     return ret
#
#
# print(something(d))


# def func1(a):
#     def func2(b, c):
#         try:
#             for e in c:
#                 if type(c) is not dict:
#                     return f'{b}.{e}', c[e]
#                 else:
#                     return func2(f'{b}.{e}', c[e])
#         except TypeError:
#             return {b: c}
#
#     ret = []
#     for e in a:
#         if type(a[e]) is not dict:
#             ret.append((e, a[e]))
#         else:
#             ret.append(func2(e, a[e]))
#     return ret
#
#
# if __name__ == '__main__':
#     d = {'a': 1, 'b': {'c': {'d': {'e': 2}}}, 'f': {'g': 2}}
#     print(d)
#     print(func1(d))


def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n - 1)

# print(factorial_recursive(1))
# print(factorial_recursive(2))
# print(factorial_recursive(3))

# try:
#     x = 2/0
# except ZeroDivisionError:
#     print('a')
#     try:
#         x = 2/0
#     except ZeroDivisionError:
#         print('a')
# finally:
#     print('b')

# print(id(None))

# # INPUT: 1 -> 2 -> 3 -> 4
# # OUTPUT: 4 -> 3 -> 2 -> 1
#
# a1 = ListNode(1)
# a2 = ListNode(2)
#
# a3 = ListNode(3)
# a2.next = a3
# a4 = ListNode(4)
# a3.next = a4
#
#
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
#
# def reverse(node):
#     # 1. получение последнего последнего элемента
#     # 2. разворачивание списка
#     last_elem = node
#     if node.next is not None:
#         last_elem = reverse(node.next)
#         node.next.next = node
#         node.next = None
#     else:
#         last_elem = node
#
#     return last_elem
#
#
# new_a1 = reverse(a1)
# new_a1.val == 4
#
# a1.next == a2
#
# # OUTPUT: 4 -> 3 -> 2 -> 1 -> 2 ->1 ...
#
# # 2 -> 1 ->

# Users:
# - id
# -firs_name
# -last_name
#
#
# Orders:
# -id
# -user_id
# -sum_order
#
#
# # выведет всех пользователей и сумму их ордеров, у которых кол-во ордеров больше 3
#
#
# SELECT User.id, Users.first_name, Users.last_name, SUM(Orders.sum_order)
# FROM Users
# JOIN Orders ON
# Users.id = Orders.user_id
# HAVING COUNT(sum_order) > 3
# GROUP BY User.id
