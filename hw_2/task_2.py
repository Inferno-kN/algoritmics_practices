def rotate_and_reverse(arr, k):
    k = k % len(arr)
    cyclic_shift = arr[-k:] + arr[:-k]
    reversed_list = cyclic_shift[::-1]
    return reversed_list

arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_and_reverse(arr, k))

print([4, 5, 1, 2, 3])

#Временная сложность: Линейная сложность O(n)
#Худший случай: Когда элементов очень много
#Лучший случай: Когда список пустой
#Средний случай: Функция должна проверить все элементы в списке независимо от их к-ва