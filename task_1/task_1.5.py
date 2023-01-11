# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

first_x = int(input('Введите X первой точки: '))
first_y = int(input('Введите Y первой точки: '))
second_x = int(input('Введите X второй точки: '))
second_y = int(input('Введите Y второй точки: '))

def Distance (x1, y1, x2, y2):
  result = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)
  return result

print(Distance(first_x, first_y, second_x, second_y))