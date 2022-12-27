def input_to_find():
    return input('Введите информацию для поиска: ')


def choose_mode():
    return input('---------------------------------------------------------------------------------------------------------\n\
"1" - Ввод новых данных, \
"2" - Поиск по базе, \
"3" - Редактирование контакта, \
"4" - Удаление контакта, \
"5" - Выход из программы \
\nВыберите комманду: ')


def new_person(id):
    name = input('Введите имя: ')
    post = input('Введите должность: ')
    salary = input('Введите зарплату: ')
    telephone = input('Введите номер: ')
    mail = input('Введите e-mail: ')

    return f'{id} | {name} | {post} | {salary} | {telephone} | {mail}'


def show_found(result):
    print('Результаты поиска: ')
    for i in result:
        print(i)


def get_base():
    with open('data.txt', "r") as file:
        return file.read()


def input_id():
    return int(input('Введите id контакта: '))


def input_edit_command():
    command = int(input('"1" - Изменить имя\
    "2" - Изменить должность\
    "3" - Изменить зарплату\
    "4" - Изменить номер телефона\
    "5" - Изменить e-mail\
    \n Введите комманду: '))

    input_info = ''
    if command == 1: input_info = input('Введите новое имя: ')
    if command == 2: input_info = input('Введите новую должность: ')
    if command == 3: input_info = input('Введите новую зарплату: ')
    if command == 4: input_info = input('Введите новый номер телефона: ')
    if command == 5: input_info = input('Введите новый e-mail: ')
    return [command,input_info]