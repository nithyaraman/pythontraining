"""
#@file         :data_type_conversion
#@Brief        : Get the input from user and convert it into different data
#                types and print it
#@Authour       :NithyaRaman

"""

float_num=float(raw_input("enter any float="))
print"this float can convert as int %d"%(int(float_num)) 
int_num=int(raw_input("enter any integer="))
print"this int convert as float %f"%(float(int_num))
name=raw_input("enter your name=")
print"name is a string ,it can convert as list"
name_as_list=list(name)
print name_as_list
print"list can convert as tuple"
list_as_tuple=tuple(name_as_list)
print list_as_tuple
print"again this tuple can convert as string"
name_str=''.join(list_as_tuple)
print name_str

