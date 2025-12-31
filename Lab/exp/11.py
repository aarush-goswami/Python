s1 = int(input("Enter ist side of triangle : "))
s2 = int(input("Enter 2nd side of triangle : "))
s3 = int(input("Enter 3rd side of triangle : "))

h = max(s1,s2,s3)
b = min(s1,s2,s3)
p = (s1+s2+s3)-(h+b)
print(f"H : {h},P : {p},B : {b}\n")

if(h**2 == (p**2 + b**2)):
    print("The triangle is right angled\n")
    s = (h+p+b)//2
    ps = s*((s-h)*(s-b)*(s-p))
    area = ps**0.5
    print("Area : ",round(area,2),"units")
else:
    print("The triangle is not right angled\n")
