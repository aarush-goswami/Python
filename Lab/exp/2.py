l = list(map(int, input("Enter list elements : ").split()))
print("Iterating in list...")
for i in l:
    print(i, end=" ")
print("\n")
dictionary = {}
n = int(input("Enter number of Key : Value pairs : "))
for i in range(n):
    k,v = input(f"Enter key value {i+1}: ").split()
    dictionary[k] = v
print("Iteration over dictonary...")
for key,value in dictionary.items():
    print(f"{key} : {value}")