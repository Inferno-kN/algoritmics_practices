def max_in_range(arr, start, end):
    absolut_index = 0
    otnos_index = 0
    max1 = arr[end]
    for i in range(start, end + 1):
        if max1 < arr[i]:
            max1 = arr[i]
            absolut_index = i
            otnos_index = absolut_index - start
    return max1, absolut_index, otnos_index

#Временная сложность: Линейная сложность
#Худший случай: Когда элементов очень много
#Лучший случай: Когда список пустой
#Средний случай: Функция должна проверить все элементы в списке независимо от их к-ва