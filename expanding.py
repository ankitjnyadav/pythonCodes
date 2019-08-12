'''
Write a function expanding(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly increases
'''


def expanding(l):
    new_l = []
    for i in range(len(l)):
        current = i
        next = i+1
        if next < len(l):
            value = l[next]-l[current]
            if value < 0:
                value = -1*value
            new_l.append(value)
    print(new_l)
    print("len(new_l)", len(new_l))
    for i in range(len(new_l)):
        current = i
        next = i+1
        print("current", current, "next", next)
        if next != len(new_l):
            print(new_l[current], new_l[next])
            if new_l[current] >= new_l[next]:
                return False
    return True


#print(expanding([1, 3, 7, 2, 9]))
print(expanding([1, 3, 7, 2, -3]))
#print(expanding([1, 3, 7, 10]))
