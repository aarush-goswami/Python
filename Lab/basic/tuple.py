# Tuple properties
'''1. It is a sequence (it allows indexing and slicing)
2. It is an ordered collection
3. It is immutable.(operations like insertiion,updation and deletion are not allowed.)
4. It may conatins duplicate elements.
5. It preserves the insertion order.
6. It may contain different types of objects'''

# Creation of tuple
'''list = [1,2,3]
t = tuple(list)
print(t,type(t))
'''
# t = 10,20,30
# print(t,type(t))

# for num in t:
#     print(num,end=" ")
# print()


# # Indexing and slicing in tuple
# print(t[0],t[-1],t[0:2],t[-2:],t[::-1],sep="\n")

# # updation and deletion is not allowed.
# list =(10,20)
# print(list)
# # list[0] = 100  ERROR
# # print(list)j,True,"James",[12,13,14])
# # t[0]= t[0] + 10   ERROR
# # print(t[0]

# t =(10,12.5,12+5)
# t[-1].append(100)

# for i in t:
#     print(i,type(i))

# t = 10,20,30,40
# a,*b,c = t
# print(f"a : {a},b: {b},c: {c}")

# a=10
# b=20
# print(a,b)
# a,b=b,a
# print(a,b)

num1 ,num2 = 0,1
for i in range(10):
    print(num1,end=" ")
    num1,num2 = num2,num1 + num2