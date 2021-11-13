from collections import Counter
import operator

def top_3_words(s):
    scores = Counter(s.split())
    print(scores)
    scores = sorted(scores.items(), key=operator.itemgetter(1))
    print(scores)
    scores = reversed(scores)
    print(scores)
    scores = list(x[0] for x in scores)
    print(scores)
    return scores[0:3]


# print(top_3_words("a a a  b  c c  d d d d  e e e e e"))#, ["e", "d", "a"])
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))#, ["e", "ddd", "aa"])
# print(top_3_words("  //wont won't won't "))#, ["won't", "wont"])