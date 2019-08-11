def binary_search(l, value, left, right):
    #if list is empty
    if right-left == 0:
        return False
    mid = (left+right)//2
    if value == l[mid]:
        return True
    if value < l[mid]:
        return binary_search(l, value, left, mid)
    else:
        return binary_search(l, value, mid+1, right)


l = list(range(1, 21))
print(l)
print("length of l:", len(l))
print(binary_search(l, 21, 1, len(l)))
