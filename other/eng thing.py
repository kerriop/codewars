def first_diff(items):
    result = []
    for i in range(1, len(items)):
        result.append(items[i] - items[i - 1])
    return result
#add tests

def first_diff(items):
    result = []
    for i in range(1, len(items)):
        result.append(items[i] - items[i - 1])
    return result


print(first_diff([1, 4, 9]))  # [3,5]
print(first_diff([10, 7, 15]))  # [-3,8]
