from lib2to3.btm_utils import tokens

f = open("abcd.txt", "r")
f_out = open("abcd1.txt", "w")
for line in f:
    f_out.write('wordcount:' + str(len(tokens)) + line)
    f.close()
    f_out.close()
