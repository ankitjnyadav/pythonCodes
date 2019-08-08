import math
#true->Prime

def sumprimes(l):
    sum = 0
    for i in l:
       if check_prime(i) and i>0:
        sum =sum+i
    return sum


def check_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
    