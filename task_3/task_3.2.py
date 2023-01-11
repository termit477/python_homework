# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

array = input('Введите значения списка: ').split()
first_array = []
for i in range(len(array)):
  first_array.append(int(array[i]))

reverse_array = first_array[::-1]

def Multy(a, b):
  mul = []
  if len(a) % 2 == 0:
    for i in range(len(a) // 2):
      mul.append(a[i] * b[i])
  else:
    for i in range(len(a) // 2 + 1):
      mul.append(a[i] * b[i])
  return mul

result = Multy(first_array, reverse_array)
print(result)
