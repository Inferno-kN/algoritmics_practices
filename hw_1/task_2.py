def fibonacci(n):
    new_lst = []
    if n < 0:
        raise ValueError

    a, b = 0, 1
    for i in range(n + 1):
        new_lst.append(a)
        a, b = b, b + a
    return new_lst

print(fibonacci(5))
print(fibonacci(10))