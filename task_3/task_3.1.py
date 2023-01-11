# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

input_array = input('Введите значения списка: ').split()

def Sum_odd (a):
    b = []
    sum = 0

    for i in range(len(a)):
        b.append(int(a[i]))

    for i in range(len(b)):
        if i % 2 == 1:
            sum += b[i]
    return sum

result = Sum_odd(input_array)
print(f'Сумма нечетных элементов:  {result}')