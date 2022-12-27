import csv

def get_base():
    with open('task_7\data.txt', "r", encoding='utf-8') as file:
        return file.read()


def add_person(person):
    try:
        with open('task_7\data.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n{person}')
        with open('task_7\data.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows([person.split(' | ')])
    except FileNotFoundError:
        with open('task_7\data.txt', 'w', encoding='utf-8') as file:
            file.write(f'{person}')
        with open('task_7\data.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows([person.split(' | ')])
