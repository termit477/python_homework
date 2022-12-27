import csv
import os.path


def get_base():
    if os.path.exists('task_8\data.txt') == False: 
        return 'Не найдено'
    else:
        with open('task_8\data.txt', "r", encoding='utf-8') as file:
            return file.read()


def update_base(new_base):
    new_base_csv = [i.split(' | ') for i in new_base]

    # new_base_csv = []
    # count=0
    # for i in new_base:
    #     new_base_csv[] = (i.split(' | '))

    with open('task_8\data.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(new_base_csv)
    with open('task_8\data.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_base))


def add_person(person):
    try:
        with open('task_8\data.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n{person}')
        with open('task_8\data.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows([person.split(' | ')])
    except FileNotFoundError:
        with open('task_8\data.txt', 'w', encoding='utf-8') as file:
            file.write(f'{person}')
        with open('task_8\data.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows([person.split(' | ')])

