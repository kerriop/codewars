def to_weird_case(string):
    words = string.split(' ')
    new_string = ''
    for word in words:
        for pos, char in enumerate(word):
            if pos % 2 == 0:
                new_string += new_string.join(char.upper())
            else:
                new_string += new_string.join(char)
        if len(words) != 1:
            new_string += new_string.join(' ')
    new_string = new_string.strip(' ')
    return new_string


print(to_weird_case('This'))
print(to_weird_case('This is a test'))
