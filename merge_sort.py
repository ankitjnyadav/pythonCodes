def merge(A, B):
    (C, m, n) = ([], len(A), len(B))
    # current postion of A and B
    (i, j) = (0, 0)
    # i+j is number of element merged so far
    while i+j < m+n:
        if i == m:  # case 1:list A is empty
            C.append(B[j])
            j = j+1
        elif j == n:  # case 2:list B is empty
            C.append(A[i])
            i = i+1
        elif A[i] <= B[j]:  # case 3:Head of A is smaller
            C.append(A[i])
            i = i + 1
        elif A[i] > B[j]:  # case 4:Head of B is smaller
            C.append(B[j])
            j = j+1
    return(C)


def merge_sort(A, left, right):
    # sort the slice A[left:right]
    if right-left <= 1:
        return A[left:right]
    if right-left > 1:
        mid = (left+right)//2
        l = merge_sort(A, left, mid)
        r = merge_sort(A, mid, right)
        return merge(l, r)


#a = list(range(1, 100, 2))+list(range(0, 102, 2))
b = [1, 9, 2, 0]
print("unsorted: ", b, end="\n\n")
print("sorted: ", merge_sort(b, 0, len(b)))
