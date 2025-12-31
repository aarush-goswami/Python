s = input("Enter string : ")
al=0
for ch in s:
    if ch.isalpha():
        al+=1

start = int(input(f"Enter start range (0 - {len(s)-1}) : "))
stop = int(input(f"Enter stop range ({start}-{len(s)-1}) : "))
step = int(input(f"Enter steps to take : (1 - {len(s)-1} : )"))

print("\nIn range characters are : ")
print(s[start:stop:step])
print(f"\nalphabets : {al}\nis alphanumeric : {s.isalnum()}")