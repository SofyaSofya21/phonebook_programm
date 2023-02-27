import user_interface as ui

def menu2_operation(database,current_file_name):
    while True: 
        ui.menu2()
        command = input('Введите команду: ')
        if command == '1': # показать весь справочник
            try:
                ui.print_phonebook(database)
            except:
                print('База данных не найдена 2.1')   
        elif command == '2': # добавить новый контакт в справочник
            try:
                database = ui.new_contact_input(database)
                ui.save_phonebook(database,current_file_name)
            except:
                print('База данных не найдена 2.2')
        elif command == '3': # поиск в справочнике
            try:
                ui.search_full_process(database)
            except:
                print('Контакт не найден')
        elif command == '4': # изменить данные контакта
            try:
                ui.search_and_correct_process(database)   
                ui.save_phonebook(database,current_file_name)                 
            except:
                print('Контакт не найден')
        elif command == '5': # удалить контакт
            try:
                ui.search_and_delete_full_process(database)   
                ui.save_phonebook(database,current_file_name)
            except:
                print('База данных не найдена 2.6')
        elif command == '9': # выход из программы
            return database
        print()


