import logger
import model
import view


def control_edit_person():
    base = logger.get_base()
    person = view.input_to_find()
    result = model.serch_person(base, person)
    view.show_found(result)
    if 'не найден' not in result[0] and len(base.split('\n')) > 1:
        find = str(view.input_id()) + ' | ' + person
        update = model.edit_person(base, find, view.input_edit_command())
        logger.update_base(update)

    elif 'не найден' not in result[0]:
        result = base.split('\n')[0]
        update = model.edit_person(base)
        logger.update_base(update)


def control_del_person():
    base = logger.get_base()
    person = view.input_to_find()
    result = model.serch_person(base, person)
    view.show_found(result)
    if 'не найден' not in result[0] and len(base.split('\n')) > 1:
        find = str(view.input_id()) + ' | ' + person
        result = model.serch_person(base, find)[0]
        update = model.del_person(base, result)
        logger.update_base(update)
    elif 'не найден' not in result[0]:
        result = base.split('\n')[0]
        update = model.del_person(base, result)
        logger.update_base(update)


def run():
    while True:
        mode = view.choose_mode()
        if mode == '1':     # Добавление
            id = model.create_id(logger.get_base())
            person = view.new_person(id)
            logger.add_person(person)

        elif mode == '2':   # Поиск
            person = view.input_to_find()
            base = logger.get_base()
            result = model.serch_person(base, person)
            view.show_found(result)

        elif mode == '3':   # Редактирование
            control_edit_person()

        elif mode == '4':   # Удаление контакта
            control_del_person()

        elif mode == '5':   # Выход из программы
            return False

        else:
            return 'Неккоретная команда'