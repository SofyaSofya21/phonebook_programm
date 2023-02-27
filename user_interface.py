import json

def menu1():
    print('Главное меню')
    print('1 - создать новую телефонную книгу')
    print('2 - импортировать телефонную книгу(json формат)')
    print('3 - скачать текущую телефонную книгу')
    print('4 - использовать текущую телефонную книгу')
    print('9 - завершение программы')

def menu2():
    print('Меню работы с телефонным справочником')
    print('1 - показать весь справочник')
    print('2 - добавить новый контакт в справочник')
    print('3 - поиск в справочнике')
    print('4 - изменить данные контакта')
    print('5 - удалить контакт')
    print('9 - выход в главное меню')

def menu3(no_id = False):
    if no_id == False:
        print('0 - id')
    print('1 - имя')
    print('2 - номер телефона')
    print('3 - дата рождения')
    print('4 - электронная почта')
    print('9 - вернуться в меню')
    # добавить общий поиск независимо от параметра 

def create_phonebook(book_name):
    fname = book_name
    BD_local = {}
    with open(fname, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(BD_local, 
                            ensure_ascii=False))
    print(f'Телефонная книга "{book_name}" создана')
    return BD_local
    
def load_phonebook(book_name):
    # загрузить из json
    fname = book_name #открываем файл
    with open(fname,'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь BD_local
    print(f'Телефонная книга "{book_name}" импортирована')
    return BD_local

def print_phonebook(database,ids_to_print = -1):
    if ids_to_print == -1:
        ids_to_print = database.keys()
    for k1,v1 in database.items():
        if k1 in ids_to_print:
            print(f'{k1}.', end = ' ')
            for k2, v2 in v1.items():
                if len(v2) != 0:
                    print(f'{k2}: {v2}', end = ' ')
            print()

def new_contact_input(database):
    name = input('Введите имя (обязательное поле для создания контакта): ')
    if len(name) > 0:
        phone = input('Введите телефон(ы) контакта через пробел: ')
        birthday = input('Введите день рождения: ')
        email = input('Введите email(ы) контакта через пробел: ')
        key = max(list(map(int,database.keys())))+1
        database[key] = {'name':name, 'phone':list(phone.split()),'birthday': birthday, 'email':list(email.split())}
    else:
        print('Вы не ввели обязательный параметр "имя". Попробуйте еще раз.')
    return database

def save_phonebook(database, fname):
    # сохранить в json
    with open(fname, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(database, 
                            ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
    print('Телефонная книга сохранена')

def search_phonebook_get_ids(search_key,database,search_requirement): # если пустая строка, то ищет все пустые строки
    search_result = []
    if search_key == 'id':
        search_result = (list((dict(filter(lambda item: item[0] == search_requirement,database.items()))).keys()))[0]
    else:
        if search_key in ['name', 'birthday']:
            search_result = list((dict(filter(lambda item: (item[1]).get(search_key).lower() == search_requirement.lower(),database.items()))).keys())
        if search_key in ['phone','email']:
            for k1 in database:
                for i in database[k1].get(search_key):
                    if i == search_requirement:
                        search_result.append(k1)
        # if len(search_result) == 0:
        #     search_result = 'Такого контакта не найдено, попробуйте изменить запрос.'
    return search_result
    
def translate_search_key(search_key):
    if search_key == 'name':
        return 'имя'
    elif search_key == 'phone':
        return 'номер телефона'
    elif search_key == 'birthday':
        return 'дату рождения'
    elif search_key == 'email':
        return 'электронную почту'
    elif search_key == 'id':
        return 'id'

def search_base(message,no_id = False):
    print(message)
    menu3(no_id)
    command = input()
    search_key = ''
    if no_id == False and command == '0':
        search_key = 'id'
    elif command == '1':
        search_key = 'name'
    elif command == '2':
        search_key = 'phone'
    elif command == '3':
        search_key = 'birthday'
    elif command == '4':
        search_key = 'email'
    # elif command == '5':
    #     search_key = 'все параметры'
    elif command == '9':
        search_key = '9'
    else: 
        search_key = 'incorrect input'
    return search_key

def search_full_process(database):
    search_key = ''
    while search_key != '9':
        search_key = search_base('По какому параметру требуется осуществить поиск?')
        if search_key == 'incorrect input':
            print('Вы ввели некорректную команду. Попробуйте еще раз')
        elif search_key in ['id', 'name', 'phone', 'birthday', 'email']: # добавить отдельно список команд?
            text = translate_search_key(search_key)
            search_req = input(f'Введите {text} для получения информации о контакте: ')
            search_res = search_phonebook_get_ids(search_key,database,search_req)
            if len(search_res) == 0:
                print('Такого контакта не найдено, попробуйте изменить запрос.')
            else:
                print_phonebook(database,search_res)
                # for i in search_res:
                #     print(f'{i} {database[i]}')
            search_key = '9'

def search_and_correct_process(database):
    search_key = ''
    while search_key != '9':
        search_key = search_base('По какому параметру требуется осуществить поиск?')
        if search_key == 'incorrect input':
            print('Вы ввели некорректную команду. Попробуйте еще раз')
        elif search_key in ['id', 'name', 'phone', 'birthday', 'email']: # добавить отдельно список команд?
            text = translate_search_key(search_key)
            search_req = input(f'Введите {text} для поиска контакта: ')
            search_res = search_phonebook_get_ids(search_key,database,search_req)
            if len(search_res) == 0:
                print('Такого контакта не найдено, попробуйте изменить запрос.')
            elif len(search_res) > 1:
                print_phonebook(database,search_res)
                # for i in search_res:
                #     print(f'{i} {database[i]}')
            search_key = '9'
    while len(search_res) > 1:
        contact_id = (input('Найдено несколько контактов. Введите id контакта, который необходимо отредактировать.\nВведите q для возврата в меню\n'))
        if contact_id != 'q':
            if contact_id in search_res:
                search_res = [contact_id]
            else:
                print('Введено некорректное значение. Попробуйте еще раз.')
        else:
            return
    search_key = ''
    while search_key != '9':
        search_key = search_base('Какое поле Вы будете редактировать?', no_id = True) # здесь надо убрать поиск по id тк его менять нельзя    
        if search_key == 'incorrect input':
            print('Вы ввели некорректную команду. Попробуйте еще раз')
        elif search_key in ['name', 'phone', 'birthday', 'email']:
            print(search_res[0])
            for k1 in database.keys():
                if k1 in search_res[0]:
                    new_value = input(f'Введите новое значения для параметра {translate_search_key(search_key)}: ')
                    if search_key in ['name','birthday']:
                        (database.get(k1))[search_key] = new_value
                    else:
                        (database.get(k1))[search_key] = list(new_value.split())
            search_key = '9'
    return database

def search_and_delete_full_process(database):
    search_key = ''
    while search_key != '9':
        search_key = search_base('По какому параметру требуется осуществить поиск контакта для удаления?')
        if search_key == 'incorrect input':
            print('Вы ввели некорректную команду. Попробуйте еще раз')
        elif search_key in ['id', 'name', 'phone', 'birthday', 'email']: # добавить отдельно список команд?
            text = translate_search_key(search_key)
            search_req = input(f'Введите {text} для поиска контакта для удаления: ')
            search_res = search_phonebook_get_ids(search_key,database,search_req)
            if len(search_res) == 0:
                print('Такого контакта не найдено, попробуйте изменить запрос.')
                continue
            elif len(search_res) == 1:
                for i in search_res:
                    print(f'{i} {database[i]}')
                action = input('Введите 0 для подтверждения удаления\nВведите q для возврата в меню\n')
            elif len(search_res) > 1:
                for i in search_res:
                    print(f'{i} {database[i]}')
                action = input('Введите 0 для удаления всех найденных контактов\nВведите q для возврата в меню\nВведите через пробел id тех контактов, которые требуется удалить\n')
            if action == '0':
                for i in search_res:
                    database.pop(i)
                print('Удаление прошло успешно.')
            elif action != 'q':
                for i in list(action.split()):
                    if i in search_res:
                        print(f'Удален контакт {database.pop(i)}')
                    else:
                        print(f'{i} - данного id нет в списке контактов для удаления')
            search_key = '9'
    return database


