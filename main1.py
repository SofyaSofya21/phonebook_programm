import user_interface as ui
import main2

print('Здравствуйте!\nВыберите действие для начала работы с телефонным справочником: ')
phonebook_name = ''
print()

while True:
    ui.menu1()
    command = input('Введите команду: ')
    if command == '1': # создать новую телефонную книгу
        try:
            while phonebook_name == '' or phonebook_name == '.json':
                phonebook_name = input('Введите название телефонной книги (без расширения): ') + '.json'
                if phonebook_name == '.json':
                    print('Нельзя создать телефонную книгу без названия.')
            print(phonebook_name)
            db = ui.create_phonebook(phonebook_name)
            db = main2.menu2_operation(db,phonebook_name)
        except:
            print('База данных не найдена 1.1') 
    elif command == '2': # импортировать телефонную книгу(json формат)
        try:
            phonebook_name = input('Введите название json файла с телефонным справочником (без расширения): ') + '.json' 
            # расширение можно задать переменной и вынести ее определение в отдельную функцию
            db = ui.load_phonebook(phonebook_name)
            db = main2.menu2_operation(db,phonebook_name)
        except:
            print('База данных не найдена 1.2')
    elif command == '3': # экспортировать текущую телефонную книгу
        try:
            ui.save_phonebook(db,phonebook_name)
        except:
            print('Вы не открыли телефонную книгу. Для работы с программой создайте новую или импортируйте существующую.')
    elif command == '4': # использовать текущую телефонную книгу
        try:
            db = main2.menu2_operation(db,phonebook_name)
        except:
            print('Вы не открыли телефонную книгу. Для работы с программой создайте новую или импортируйте существующую.')
    elif command == '9': # завершить программу
        print('Благодарим за использование нашей программы! Хорошего дня!')
        exit()
    print()

