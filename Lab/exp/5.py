mat = []

m = int(input("Enter rows for matrix : "))
n = int(input("Enter cols for matrix : "))

for i in range(m):
    r = []
    for j in range(n):
        x = int(input(f"Enter element [{i}][{j}] : "))
        r.append(x)
    mat.append(r)
for i in range(m):
    for j in range(n):
        print(mat[i][j], end=" ")
    print("")

r = int(input("Enter row to reverse : "))
r -= 1

if 0<= r < m:
    mat[r] = mat[r][::-1]
    for i in range(m):
        for j in range(n):
            print(mat[i][j], end=" ")
        print("")
else:
    print("Enter correct row \n")