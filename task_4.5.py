# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

from sympy import simplify
from task_4_polinom import create_polinom
from task_4_polinom import create_file

degree = int(input('Введите степень: '))

pol1 = create_polinom(degree)
pol2 = create_polinom(degree)

name_file_pol1 = 'task_4.5_1'
name_file_pol2 = 'task_4.5_2'
name_sum = 'task_4.5_sum'

create_file(pol1, file = name_file_pol1)
create_file(pol2, file = name_file_pol2)

with open(f'{name_file_pol1}.txt', 'r') as f1:
  f_pol = f1.read()
  print(f'Первый полином: {f_pol}')
  f1.close()

with open(f'{name_file_pol2}.txt', 'r') as f2:
  s_pol = f2.read()
  print(f'Второй полином: {s_pol}')
  f2.close()

sum = str(simplify(f_pol + '+' + s_pol))
print(f'Сумма: {sum}')

with open(f'{name_sum}.txt', 'w') as s:
  s.write(sum)
  s.close()
