import random


def selection_sort(l):
    #scan slices l[0:len(l)],l[1:len(l)]
    for start in range(len(l)):
        #find min value in slice
        minpos = start
        for i in range(start, len(l)):
            if l[i] < l[minpos]:
                #change the index
                minpos = i

        #and move it to the start of the slice
        (l[start], l[minpos]) = (l[minpos], l[start])
    return l


l = list(range(random.randint(1, 100)))
l.reverse()
print("l:", l)
print("length of l:", len(l))
print(selection_sort(l))
