def count_ones(n):
    if n < 0:
        raise ValueError
    result = 0
    while n:
        result = result + n % 2
        n = n // 2
    return result


print(count_ones(0))
print(count_ones(5))
print(count_ones(4))