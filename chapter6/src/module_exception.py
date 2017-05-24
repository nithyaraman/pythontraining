""" Print 'Module not installed' when 'import gnulinux'"""


try:
    import gnulinux

except ImportError:
    print "Module not installed"
