# F = (°C × 9/5) + 32.
c = float(input("Enter temperature in C : "))
f = (c * (9/5)) + 32
print(f"in F : {round(f,2)}")

f = float(input("Enter temperature in F : "))
c = (f - 32)*(5/9)
print("in C : ",round(c,2))