# from urllib.parse import urlparse

# def domain_name(url):
#     ret = urlparse(url).netloc.split('.')
#     if ret == ['']:
#         ret = urlparse(url).path
#         ret = ret.split('.')
#     print(ret)
#     if ret[0] == 'www':
#         return ret[1]
#     else:
#         return ret[0]

import re


def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


# print(domain_name("http://github.com/carbonfive/raygun"))  # == "github"
# print(domain_name("http://www.zombie-bites.com"))#== "zombie-bites"
print(domain_name("https://www.cnet.com"))  # == "cnet"
print(domain_name("www.xakep.ru"))  # , "xakep")
print(domain_name("http://google.co.jp"))  # , "xakep")
