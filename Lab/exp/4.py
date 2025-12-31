def linear_search(list, tar):
    if tar in list:
        return list.index(tar)
    return -1


def binary_search(lst, tar):
    lst = sorted(lst)
    l = 0
    r = len(lst) - 1
    while l <= r:
        mid = (l + (r - l)) // 2
        if lst[mid] == tar:
            return mid
        elif lst[mid] > tar:
            r = mid - 1
        elif lst[mid] < tar:
            l = mid + 1
        else:
            return -1


l = list(map(int, input("Enter list elements : ").split()))
tar = int(input("Enter element to search : "))
ch = int(input("1.Linear search \t 2.Binary search"))
if ch == 1:
    res = linear_search(l, tar)
    if res != -1:
        print("Found at ", res)
    else:
        print("Not found")
else:
    res = binary_search(l, tar)
    if res != -1:
        print("Found at ", res)
    else:
        print("Not found")
