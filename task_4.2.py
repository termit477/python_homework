# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

number = int(input('Введите число: '))

def NOD(a: list) -> list:
    i = 2
    simple = []
    while a != 1:
        while a % i == 0:
            simple.append(i)
            a //= i
        i += 1
    return simple    

    
result = NOD(number)
print(f'Простые делители числа {number} - {result}')
print(f'Уникальные делители числа {number} - {list(set(result))}')
