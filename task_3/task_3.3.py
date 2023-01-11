# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

array = [1.1, 1.2, 3.1, 5, 10.01]

def Fraction(a: float) -> float:
  frac = str(a).split('.')
  return float('0.' + frac[1])

def Diff (list1):
  result_array = [Fraction(i) for i in list1 if int(i) != float(i)]
  print(result_array)
  return max(result_array) - min(result_array)

result = Diff(array)
print(result)
