""" print the dates between March-2017 to April-2017 using datetime"""

# can print date and time from any month of the year to any month of
# another year

import calendar


from_month = int(input("start with month= "))
from_yr = int(input("start with the year= "))

year1 = from_yr


to_month = int(input("end with month= "))
to_yr = int(input("end with the year= "))

count = 1

while (from_yr <= to_yr):
    if year1 == from_yr:
        count = from_month
    while(count <= 12):
        cal = calendar.month(from_yr, count)
        print cal, "\n"
        if count == 12:
            from_yr += 1
            count = 1
        else:
            count += 1
        if to_yr == from_yr and count > to_month:
            break
    if to_yr == from_yr and count > to_month:
        break
