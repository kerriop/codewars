def is_isogram(string):
    my_list = [i for i in string.lower()]
    return sorted(my_list) == sorted(list(set(my_list)))

print(is_isogram('isogram'))
# print(is_isogram('moOse'))