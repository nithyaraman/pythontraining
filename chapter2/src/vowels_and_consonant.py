#"""
#@File         :vowels_and-consonant
#@Brief        :write the program to print vowels and consonant letters from#               'gnulinux'
#@Author       :NithyaRaman
#"""
vowel=['a','e','i','o','u']
for var in 'gnulinux':
   if var in vowel:
      print "%c=vowel"%var
   else: 
      print "%c=consonant"%var  
    
