# count number of lines

def countline(filename):
      num_line=0
      with open (filename,'r') as files:
          for i in files:
             num_line+=1
      return num_line

