def is_palindrome(x) -> bool:
    if x == "":
        raise ValueError
    x = str(x)
    return x == x[::-1]

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(7))