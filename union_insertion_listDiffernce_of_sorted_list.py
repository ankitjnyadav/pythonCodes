from insertion_sort import insertion_sort

# union of 2 sorted list


def union_of_sorted_list(A, B):
    U = []
    (i, j, m, n) = (0, 0, len(A), len(B))
    while i+j < m+n:
        if i == m:  # case 1:list A is empty
            U.append(B[j])
            j = j+1
        elif j == n:  # case 2:list B is empty
            U.append(A[i])
            i = i+1
        elif A[i] == B[j]:  # case 3:list A and B have same element
            j = j+1
        elif A[i] < B[j]:  # case 4:Head of A is smaller
            U.append(A[i])
            i = i + 1
        elif A[i] > B[j]:  # case 5:Head of B is smaller
            U.append(B[j])
            j = j+1
    return(U)

# intersection of two sorted list


def intersection_of_sorted_list(A, B):
    I = []
    (i, j, m, n) = (0, 0, len(A), len(B))
    while i+j < m+n:
        # case 1:list A and B have same element
        if i == len(A) or j == len(B):
            break
        elif A[i] == B[j]:
            if A[i] == B[j]:
                j = j+1
            I.append(A[i])
            i = i+1
        elif A[i] < B[j]:  # case 2:Head of A is smaller
            i = i + 1
        elif A[i] > B[j]:  # case 3:Head of B is smaller
            j = j+1
    return(I)

# list difference of 2 sorted list


def list_difference_of_sorted_list(A, B):
    ld = []
    for value_a in A:
        if value_a not in B:
            ld.append(value_a)
    return(ld)


a = insertion_sort([7, 1, 5, 2, 3, 6])
b = insertion_sort([3, 8, 6, 20, 7])
print(a)
print(b)
print(intersection_of_sorted_list(a, b))
print(union_of_sorted_list(a, b))
print(list_difference_of_sorted_list(b, a))
