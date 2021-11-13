import re


def top_3_words(s):
    l = [x.lower() for x in re.split("[^a-z'A-Z]", s) if x != ""]
    l = [x for x in l if len(x.replace("'", "")) != 0]
    d = {i: l.count(i) for i in l}
    l = sorted(d.items(), key=lambda i: i[1], reverse=True)
    ll = len(l)
    if ll > 3:
        ll = 3
    return [x[0] for x in l[:ll]]


# print(top_3_words("a a a  b  c c  d d d d  e e e e e"))#, ["e", "d", "a"])
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))  # , ["e", "ddd", "aa"])
# print(top_3_words("  //wont won't won't "))  # , ["won't", "wont"])
