# f = open("new.txt",'x')

with open("new.txt", "a") as n:
    n.write("This is the first line\n")

with open("new.txt", "a") as n:
    n.write("This is the second line")

with open("new.txt", "r") as n:
    print(n.read())

with open("new.txt","w") as n:
    n.write("using write")

with open("new.txt", "r") as n:
    print(n.read())
n.close()
import os
os.remove("new.txt")