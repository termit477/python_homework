# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x**2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x**3 + 4*x*2 + 4*x + 5 = 0 5'. 


from task_4_polinom import create_polinom
from task_4_polinom import create_file

k = int(input('Введите коэффициент: '))

result_polinom = create_polinom(k)
print(f'Полином: {result_polinom}')
create_file(result_polinom)