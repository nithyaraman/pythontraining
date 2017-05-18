"""
@File       : loop_break_continue
@Brief      : Write the program to break the loop if user give 'n' as input, if 'y' continue
@Authour    : NithyaRaman
"""
print "loop to print 1 to 10"
count = 1
yes = ['y', 'Y']
no = ['n', 'N']
while (count < 11):
    print count
    count += 1
    letter = raw_input("do you want to continue(y/n):")
    if letter in yes:
        continue
    elif letter in no:
        break
