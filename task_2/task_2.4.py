# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите N: '))
mass = []
pos = []
result = 1

for i in range(-n, n + 1):
    mass.append(i)
print(mass)

position = open('task_2.4.read.txt', 'r')
for line in position:
    pos.append(int(line))
position.close()

for i in range(len(pos)):
    if pos[i] <= (n * 2):
        result *= mass[pos[i]]

print(result)