def big_digit(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
    return [1] + digits

digits = [1, 2, 3]
result = big_digit(digits)
print(result)

#Временная сложность: Линейная сложность O(n)
#Худший случай: Когда элементов очень много
#Лучший случай: Когда список пустой
#Средний случай: Функция должна проверить все элементы в списке независимо от их к-ва