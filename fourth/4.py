import re

s = '2**100'

if not re.search('[a-zA-Z]', s):
    res = eval(s)
    print(res)