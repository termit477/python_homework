# Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

import math

multi = int(input('Введите точность ввода числа Пи: '))

print(f' Число Пи с точностью {multi} знаков после запятой - {round(math.pi, multi)}')