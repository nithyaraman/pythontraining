"""Print 'Invalid key!' when d['os_ver'] on d={'os':'linux'}"""


dict1 = {'os': 'linux'}

try:
    key = input("enter key : ")
    print dict1[key]


except KeyError:
    print "invalid key!"

except NameError:
    print "name error :type key inside coats('')"
