from random import randint
import sys
intfile=open("integers.txt", "a+")
for i in range(0,int(sys.argv[1])):
    linestring=""
    for j in range(0,int(sys.argv[2])):
        num=randint(0,9)
        linestring+=str(num)+" "
    intfile.write(linestring+"\r\n")
    intfile.flush()
intfile.close()
