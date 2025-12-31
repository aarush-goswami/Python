# sum2 = lambda x,y:x+y
# print(sum2(12,13))

# p = lambda x,y:x**y
# print(p(2,3))

# s = lambda *args: sum(args)
# print(s(1,2,3,4,5))

# l = ["axe","battle","raju","a"]

# l.sort(key= lambda n:n[0])
# print(l)

d = {
    "sum": lambda x,y : x+y,
    "sub": lambda x,y : x-y,
    "mul": lambda x,y : x*y,
    "div": lambda x,y : x/y
}

print(d["sum"](1,2))
print(d["mul"](3,3))