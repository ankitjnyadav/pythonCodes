'''
Write a function accordian(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements alternates between increasing strictly and decreasing strictly.
'''


def accordian(l):
    new_l = []
    flag = None
    print(len(l))
    for i in range(len(l)):
        if i+1 != len(l):
            x = abs(l[i+1]-l[i])
            new_l.append(x)
    print(new_l)
    flag = check(new_l)
    return flag


def check(new_l):
    flag = None
    i = 0
    #value is decrease
    if new_l[i] > new_l[i+1]:
        flag = increase(new_l[i+1:])
    elif new_l[i] < new_l[i+1]:
        flag = decrease(new_l[i+1:])
    else:
        flag = False
    return flag


def increase(inc_l):
    i = 0
    #while i < len(inc_l):
    if len(inc_l) == 1:
        return True
    if inc_l[i] < inc_l[i+1]:
        value = inc_l[i+1]
        flag = decrease(inc_l[i+1:])
        return flag
    else:
        return False


def decrease(dec_l):
    i = 0
    #while i < len(dec_l):
    if len(dec_l) == 1:
        return True
    if dec_l[i] > dec_l[i+1]:
        value = dec_l[i+1]
        flag = increase(dec_l[i+1:])
        return flag
    else:
        return False


print(accordian([1, 5, 2, 8, 3]))
print(accordian([-2, 1, 5, 2, 8, 3]))
print(accordian([1, 5, 1]))
print(accordian([1, 5, 2, 8, 1]))
