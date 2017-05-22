"""write the program to print vowels
 and consonant letters from gulinux'"""


vowel = ['a', 'e', 'i', 'o', 'u']
vowel_list = []
consonant_list = []


for var in 'gnulinux':
    if var in vowel:
        vowel_list.append(var)
    else:
        consonant_list.append(var)


print "cosonant letters in gnuliunx\n", consonant_list
print "vowel letters in gnuliunx \n", vowel_list
