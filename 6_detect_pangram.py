import string


def is_pangram(s):
    return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())
    # return set(string.ascii_lowercase) == set('abcdefghijklmnopqrstuvwxyz')


pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))
