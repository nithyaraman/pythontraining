"""Filter the string elements from data = [100, '200', 'gnon <lambda> at 0x7f2954eec500>, [100, '200', 'gnu', 0]]
ing filter()
with help of lambda and type functions"""


import string

data = ['100', '200', 'gnu', '0']
result = filter(lambda x: str.isdigit(x), data)

print result
