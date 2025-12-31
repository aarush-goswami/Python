# s = "Python"
# print(s[1:4])
# print(s[-1::-1])
# # print(dir(str))

# s="WELCOME"
# print(s[-2:]+s[2:5]+s[0:2])
# print(s)

# s="abracadabra"
# st=s[0]
# for c in s:
#     if c == s[0]:
#         st+="$"
#     else:
#         st+=c
# print(st)

#functions
#case manipulaton functions
# s="python string functions"
# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.swapcase())
# print(s.count('o',2,8))
# print(s.endswith(s))
# print(s.index("o",5,22))

# #formatting function
# s="Hello seperate me"
# print(s.center(20,"-"))
# print(s.ljust(20,"-"))
# print(s.rjust(20,"-"))
# print(s.split())
# l = s.split(" ")
# s="-".join(l)
# print(s)
s="  xyzk"
print(s.lstrip())
s = "xyzk  "
print(s.rstrip())
s= "malayalam"
print(s.strip("ma")) #remove only trailing characters (default " ")
print(s.replace("l","k"))
s="abracadabra"
print(s[0]+s[1:].replace("a","$"))
#string formatting
# name = "xykl"
# age = 19
# print("I am %s and i am %s years old"%(name,age))
# print("I am {} and i am {} years old".format(name,age))
# print(f"I am {name} and i am {age} years old")
