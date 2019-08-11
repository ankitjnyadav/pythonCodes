import random


def insertion_sort(l):
    for sliceEnd in range(len(l)):
        '''
        build longer and longer sorted slices
        In each iteration l[0:sliceEnd] already sorted
        move first element after sorted slice left till it's in the correct place
        '''
        pos = sliceEnd
        while pos > 0 and l[pos] < l[pos-1]:
            (l[pos], l[pos-1]) = (l[pos-1], l[pos])
            pos = pos-1

    return l


l = list(range(random.randint(1, 100)))
l.reverse()
#l=[4,5,3,2,1,19,34,4,12,11,4]
print("l:", l)
print("length of l:", len(l))
print(insertion_sort(l))
