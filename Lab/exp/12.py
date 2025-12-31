def return_max(*args):
    return max(args)


def is_Armstrong(num):
    l = len(str(num))

    temp = num
    s = 0
    while temp >0:
        d = temp%10
        s+= d**l
        temp//=10
    return s == num

nums = list(map(int, input("Enter 3 numbers : ").split()))
print(f"Max. no. : {return_max(*nums)}")

print(is_Armstrong(int(input("Enter number to check armstrong : "))))