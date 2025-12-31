# abs,len,min,round,isalnum,type()

#abs
x = int(input("Enter Number : "))
y = int(input("Enter Number : "))
print(abs(x),abs(y))

#len
s = input("\nEnter string : ")
print("length : ",len(s))

#min
x = list(map(int,input("\nEnter list elements : ").split()))
y = input("Enter alphabets : ")
print("min x : ",min(x))
print("min y : ",min(y))

#round
x = float(input("\nEnter number : "))
y = float(input("Enter number : "))

print(f" x : {round(x,2)} ,y : {round(y)}")

#type
x = 12
y = 1.99
a = "x"
b = False
print(f"\nx : {type(x)}\ny : {type(y)}\na : {type(a)}\nb : {type(b)}\n")

#isalnum
x = input("\nEnter characters : ")
y = input("Enter characters : ")

print(f"x (alnum): {x.isalnum()}, y (alnum) : {y.isalnum()}")