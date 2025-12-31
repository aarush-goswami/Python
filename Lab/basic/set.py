# s = set([1,3,2,4,3,5])
# x = set([1,2,3])

# # for i in range(len(s)):
# #     print(s.pop())
# # print(s)

# # print(s.issuperset(x))
# # print(x.issubset(s))
# # print(s.isdisjoint(x))

# s = frozenset([1,2,3,4,5,6])
# print(s)

# for i in dir(frozenset):
#      if(i.startswith("__")):
#           pass
#      else:
#           print(i)

# Line1 = "Manik"
# Line2  = "Sharma"
# Line3 = Line1 + Line2
# print("AND" in Line3)

arr =[[1,2,3,4],
      [4,5,6,7],
      [8,9,10,11],
      [12,13,14,15]
]
for i in range(0,4):
    print(arr[i].pop())
a = [[]]*3
print(a)