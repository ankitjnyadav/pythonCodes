def intreverse(n):
    reverse = 0
    while(n > 0):
        reminder = n % 10
        reverse = (reverse*10)+reminder
        n = n//10
    return reverse
