import fileinput
import re
#run 1 an 3

file = open("testinp.txt","r")
test = file.read()
file2 = open("test1a2.txt","w")
#file2.write(re.sub(r'([\n ])\'((.|\n)*?)((\.|\?|\-|\!|\,)[ ]*\')', r'\1"\2\5"', test))
file2.write(re.sub(r'Mr.', r'Mr@', test))
file2.close()

file = open("test1a2.txt","r")
test = file.read()
file2 = open("test1a2.txt","w")
file2.write(re.sub(r'([A-Z])\.', r'\1@', test))
file2.close()


file = open("test1a2.txt","r")
test = file.read()
file2 = open("test1a2.txt","w")
file2.write(re.sub(r'([\n \'])\b([A-Z])((.|\n)*?)((\.|\?|\!))', r'<s>\1\2\3\5</s>', test))
file2.close()


file = open("test1a2.txt","r")
test = file.read()
file2 = open("test1a2.txt","w")
file2.write(re.sub(r'@', r'.', test))
file2.close()
