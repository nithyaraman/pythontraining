""" Print 'Can not divide.' when 100/0 """


def divide(num, dem):
    result = num / dem
    return result

try:
    print "division"
    ans = divide(int(input("enter numerator:")),
                 int(input("enter denominator:")))
    print "answer is", ans

except ZeroDivisionError:
    print "can not divide"
