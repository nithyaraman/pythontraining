""" check the 'n' and 'l' is available or not in 'gnu'"""


word = "gnu"
n_count = word.count('n', 0, len(word))
l_count = word.count('l', 0, len(word))

if n_count is 0:
    print "n is not available"
else:
    print "n is available %d time" % n_count

if l_count is 0:
    print "l is not available"
else:
    print "l is available %d time" % l_count
