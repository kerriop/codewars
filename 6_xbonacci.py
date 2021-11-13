def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(10))

def Xbonacci(signature, n):
    result = signature[:]

    for x in range(n - len(signature)):
        current_fib = 0
        start = len(result) - len(signature)
        for y in result[start:]:
            current_fib += y
        result.append(current_fib)
    return result[:n]


print(Xbonacci([0, 1], 10))  # , [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(Xbonacci([1, 1], 10))  # , [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# for i in range(1,11):
#     print(i) # 1..10
