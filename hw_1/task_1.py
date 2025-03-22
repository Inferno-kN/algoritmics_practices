def factorial(n):
    factor = 1
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        raise ValueError
    else:
        for i in range(2, n+1):
            factor *= i
        return factor

print(factorial(0))
print(factorial(5))

