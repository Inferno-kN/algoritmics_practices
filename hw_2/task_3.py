def reverse_even_elements(arr):
    new_lst = []
    massive = []
    for i in arr:
        if i % 2 == 0:
            new_lst.append(i)
    reversed_list = new_lst[::-1]  # здесь я сделал реверсированный список
    for i in arr:
        if i % 2 == 0:
            massive.append(reversed_list)  # и тут я туплю что-то разобрать бы
        else:
            massive.append(i)
    return massive
#Временная сложность: Линейная сложность O(n)
#Худший случай: Когда элементов очень много
#Лучший случай: Когда список пустой
#Средний случай: Функция должна проверить все элементы в списке независимо от их к-ва




