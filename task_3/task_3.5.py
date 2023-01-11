# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

number = int(input('Введите число: '))

def Fibonacci(a):
    if a == 1: return [0]        
    array = [0,1]
    for i in range(2, a):
        array.append(array[i-1] + array[i-2])
    reverse_array = array[::-1]
    reverse_array.pop()
    for i in range(len(reverse_array)):
        reverse_array[i] = -reverse_array[i]
    result_array = reverse_array + array
    return result_array

result = Fibonacci(number)
print(result)