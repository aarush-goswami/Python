# l1 = [11,1,2,"abc",[1,2,3]]
# print(l1)
# print(l1.index([1,2,3]))
# print(l1[-1:])
# Write a program to accept total numbers of list elements from user then accept elements of list from user and print

# l1 =  list(map(int,input("Enter numbers in the list : ").split()))
# print(l1)

# n = int(input("Enter number of ele : "))
# li = []
# for i in range(n):
#     num = int(input(f"Enter number {i+1} : "))
#     li.append(num)


# l = [7, 5, 2, 9, 10, 90, 36]
# print("List in ascending order is ",sorted(l))

# print("List in descending order is ",sorted(l)[::-1])

# l = [7, 5, 2, 9, 10, 90, 36]

# for i in range(len(l)):
#     num = l[i]
#     idx = i
#     for j in range(i+1, len(l)):
#         if num > l[j]:
#             idx=j
#             num = j

#     l[idx] = l[i]
#     l[i] = num

# print("List in ascending order is",l)

# l = [1,2,3,4,5,6,7]
# print(l)
# l.append(8)
# print("append : ",l)
# l.insert(3,99)
# print("insert : " ,l)
# l.extend([9,10,11])
# print("extend : ",l)
# l.remove(99)
# print("remove : ",l)
# l.pop()
# print("pop wi : ",l)
# l.pop(-1)
# print("pop -1 : ",l)
# del(l[-1])
# print("del -1 : ",l)
# l.sort()
# print("sort : ",l)
# l.sort(reverse=True)
# print("sort rev : ",l)
# print(l.index(7))
# l.clear()
# print(l)

"""questions
1 accept integer list until -ve ,sort element and print max el print smallest el print second largest merge two lists now remove
all elements

2. create 2 lists with int elements and create a 3rd list with elements as result of sum of 2 lists at a specific position
3.create a list and"""

# 1
# l = []
# print("Enter list elements , -ve to stop")
# while True:
#     ch = int(input("Enter element : "))
#     if ch < 0:
#         break
#     else:
#         l.append(ch)
# print("list : ",l)
# l.sort()
# print("\nsorted list : ",l)
# print(f"Max : {max(l)}\tMin : {min(l)}")

# max2 = 0
# for i in l:
#     if max2 <= i and i != max(l):
#         max2 =i
# print("2nd largest : ",max2)
# l2 = ["merged","list"]
# l.extend(l2)
# print("Extended : ",l,"\n\n")

#2
l2 = list(map(int,input('\nEnter integers for l1 (space seperated) : ').split()))
l3 = list(map(int,input('\nEnter integers for l2 (space seperated) : ').split()))
l4 = []
if (len(l3) > len(l2)):
    l2,l3 = l3,l2
for i in range(len(l2)):
    if i < len(l2) and i<len(l3):
        l4.append(l2[i]+l3[i])
    else:
        l4.append(l2[i])
print(l4)