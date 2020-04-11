def factorial_cal(n):
    if n in (0,1):
        return 1
    else:
        return n * factorial_cal(n-1)
print(factorial_cal(5))
