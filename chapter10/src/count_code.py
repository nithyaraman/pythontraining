"""Return the number of times that the string "code"appears 
anywhere inthe given string, except we'll accept any letter
 for the 'd', so "cope" and "cooe" count."""


def find_word(str1):
    count = 0
    place = 0
    i = 0

    while i < len(str1):
        rv = str1.find("c", place, len(str1))
        if rv is -1:
            break
        else:
            if str1[rv + 1] == 'o' and str1[rv + 3] == 'e':
                count += 1
                place += rv + 1
                i += 1
    return count


str1 = raw_input("enter string:")
count = find_word(str1)

print count
