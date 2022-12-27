
def serch_person(base, find):
    base = base.split('\n')
    serch = True
    result = []
    for i in base:
        if str(find) in i:
            result.append(i)
            serch = False
    if serch:
        result.append(f'Контакт |{find}| не найден')
    return result


def create_id(base):
    if base == 'Не найдено': 
        return 1
    else: 
        base = base.split('\n')[len(base.split('\n'))-1]
        id = int(base.split(' | ')[0]) + 1
        return id


def edit_person(base, find_item, new_info):
    base = base.split('\n')
    index = 0
    for i in base:
        index += 1
        if find_item in i:
            person = i
            break
    new_person = person.split(' | ')
    new_person[new_info[0]] = new_info[1]
    print(new_person)
    new_person = ' | '.join(new_person)
    print(new_person)
    base[index-1] = new_person
    print(base)
    return base


def del_person(base, result):
    base = base.split('\n')
    base.remove(result)
    return base
    

