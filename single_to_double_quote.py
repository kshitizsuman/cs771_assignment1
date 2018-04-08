import fileinput
import re
#run 1 an 3

file = open("testinp.txt","r")
test = file.read()
file2 = open("inp.txt","w")
file2.write(re.sub(r'([\n ])\'((.|\n)*?)((\.|\?|\-|\!|\,)[ ]*\')', r'\1"\2\5"', test))
file2.close()