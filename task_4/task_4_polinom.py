import sympy
from random import randint as rnd

def create_polinom (a, simple = True):
    polinom = ''
    simple = True
    for i in range(a, -1, -1):
        polinom += f'{rnd(0,2)}*x**{i}+'
        if i == 0:
            polinom += f'{rnd(0,100)}*x**{i}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom) 

def create_file(polinom, file = 'task_4.4'):
  with open (f'{file}.txt', 'w') as f:
    f.write(polinom)
    f.close()
