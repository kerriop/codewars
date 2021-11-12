# def duplicate_encode(word):
#     ans = ''
#     word = word.lower()
#     for ch in word:
#         print(ch)
#         if word.count(ch) == 1:
#             print(word)
#             ans += ans.join('(')
#         else:
#             ans += ans.join(')')
#     return ans

from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    ans = ''
    for c in word:
        if counter[c] == 1:
            ans += ans.join('(')
        else:
            ans += ans.join(')')
    return ans

print(duplicate_encode("din")) #  "(((")
print(duplicate_encode("qGXDTYgH bVqSpUKiSuKJYKKFm)wiV@PjgK"))# == '))((())((())))))))))))))(((())())))')#  "(((")
# print(duplicate_encode("recede")) #  "(((")
# print(duplicate_encode("Success")) #  "(((")
# print(duplicate_encode("(( @")) #  "(((")