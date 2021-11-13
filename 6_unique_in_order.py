def unique_in_order(iterable):
    res = ''
    prev = ''
    res2 = []
    for ch in iterable:
        if prev != ch:
            if type(ch) == str:
                res += res.join(ch)
            else:
                res2.append(ch)
            prev = ch
    return list(res) or res2

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

print(unique_in_order('AAAABBBCCDAABBB'))  # , ['A','B','C','D','A','B']))
print(unique_in_order([1, 2, 2, 3, 3]))  # , ['A','B','C','D','A','B']))
