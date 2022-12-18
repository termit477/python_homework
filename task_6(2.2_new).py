# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# С использованием enumerate, map, lambda

number = int(input('Введите число: '))

result = list(enumerate(map(lambda x: 3*x +1, range(1,number + 1))))
print(result)
