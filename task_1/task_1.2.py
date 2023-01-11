# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('Введите X: '))
y = bool(input('Введите Y: '))
z = bool(input('Введите Z: '))

def Check (a, b, c):
  result = (not(a or b or c)) == (not a and not b and not c)
  print(result)

Check(x, y, z)