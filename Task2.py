def check_div(list_n, div_numeric):
    result = [] #Массив чисел
    for numeric in list_n: #Проходим по исходному массиву
        if numeric % div_numeric == 0: #Проверяем делимость на нужную цифру
        #Метод append() в Python добавляет элемент в конец списка
            result.append(numeric)
    return result
#Запись в массив
list_n = []
print('Введите количество цифр и значения: ')
#range() генерируем последовательность чисел с определенным шагом
#далее их можно легко перебирать с помощью цикла for.
for i in range(int(input())):
    list_n.append(int(input()))
#Вызов функции
print('Делятся на 2:', end=' ')
print(check_div(list_n, 2))
print('Делятся на 3:', end=' ')
print(check_div(list_n, 3))
print('Делятся на 5:', end=' ')
print(check_div(list_n, 5))
#Savoskina
