# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


number = input('Введите число: ')
result = 0

for i in number:
    if i != '.':
        result += int(i)
        
print(f'Сумма чисел равна - {(result)}')