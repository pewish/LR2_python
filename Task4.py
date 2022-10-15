def sqr_n(a, n):
    eps = 0.001 #Точность
    xi = 1 #Начальное значение

    while True:
        xi_1 = (((n-1) * xi) + (a / (xi ** (n-1)))) / n #Расчёт по формуле
        if abs(xi_1 - xi) < eps: #Проверка точности
            break
        xi = xi_1
    return xi_1
#Ввод значений
a = float(input('Число: '))
n = int(input('Степень: '))
#Вывод результатов
print('Корень =', end=' ')
print(sqr_n(a, n)
#Savoskina
