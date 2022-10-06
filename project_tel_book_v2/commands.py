import csv
import json
import datetime

path_logs = '/Users/ivanfedulov/Desktop/python ed/project_tel_book_v2/logs.txt'
path_json = '/Users/ivanfedulov/Desktop/python ed/project_tel_book_v2/db.json'
path = '/Users/ivanfedulov/Desktop/python ed/project_tel_book_v2/db.csv'
time = datetime.datetime.now().replace(microsecond=0)

def import_contacts():
    logs = open(path_logs, 'a')
    logs.write(f'{time} - Нажата кнопка "Импортировать старые контакты"!\n')
    with open(path_json,'r') as firstdb:
        data = json.load(firstdb)
    data_list = []
    for i in data:
        data_list += (list(zip(i.keys(), i.values())))
    with open(path, 'a') as db:
            writer = csv.writer(db)
            for i in data_list:
                writer.writerow(i)
    logs.write('Контакты импортированы!\n')
    logs.close()
    print(f'{time} - Контакты импортированы!')

def create_contact():
    logs = open(path_logs, 'a')
    logs.write(f'{time} - Нажата кнопка "Создать контакт"!\n')
    name = input('\nВведите имя контакта: ')
    logs.write(f'{time} - Введено имя контакта {name}!\n')
    phone = input(f'Введите номер телефона контакта {name}: ')
    logs.write(f'{time} - Введен номер контакта {name}!\n')
    list_data = [name, phone]
    with open(path, 'a', newline='') as db:
        writer = csv.writer(db, delimiter=',')
        writer.writerow(list_data)
    logs.write(f'{time} - Контакт {name} добавлен!\n')
    logs.close()
    print('Контакт добавлен!')

def find_contact():
    logs = open(path_logs, 'a')
    logs.write(f'{time} - Нажата кнопка "Найти контакт"!\n')
    find_name = input('\nВведите имя для поиска контакта: ')
    logs.write(f'{time} - Введено имя контакта {find_name}!\n')
    with open(path, 'r', newline='') as db:
        reader = csv.reader(db, delimiter=',')
        for row in reader:
            if find_name == row[0]:
                print(*row)
    logs.write(f'{time} - Контакт {find_name} добавлен!\n')
    logs.close()
    print('Контакт найден!')

def del_contact():
    logs = open(path_logs, 'a')
    logs.write(f'{time} - Нажата кнопка "Удалить контакт"!\n')
    name = input('\nВведите имя контакта, который хотите удалить: ')
    logs.write(f'{time} - Введено имя контакта {name}!\n')
    lst = []
    with open(path, 'r') as db:
        reader = csv.reader(db, delimiter=',')
        for row in reader:
            lst.append(row)
    for i in lst:
        if name in i:
            lst.remove(i)
            break
    with open(path, 'w') as db:
        writer = csv.writer(db, delimiter=',')
        writer.writerows(lst)
    logs.write(f'{time} - Контакт {name} добавлен!\n')
    logs.close()
    print('Контакт удален!')

def change_contact():
    logs = open(path_logs, 'a')
    logs.write(f'{time} - Нажата кнопка "Изменить контакт"!\n')
    name = input('\nВведите имя контакта, который хотите изменить: ')
    logs.write(f'{time} - Введено имя контакта {name}!\n')
    choice = input('Что вы хотите изменить?\n1. Имя\n2. Номер телефона\n :')
    match choice:
        case '1':
            logs.write(f'{time} - Выбрано изменить имя контакта!\n')
            change_name = input('Введите измененное имя: ')
            logs.write(f'{time} - Введено измененное имя контакта {name}!\n')
            lst = []
            with open(path, 'r') as db:
                reader = csv.reader(db, delimiter=',')
                for row in reader:
                    lst.append(row)
            for i in lst:
                if name in i:
                    i[0] = change_name
                    break
            with open(path, 'w') as db:
                writer = csv.writer(db, delimiter=',')
                writer.writerows(lst)
            logs.write(f'{time} - Имя контакта {name} изменено!\n')
            logs.close()
            print('Имя контакта изменено!')
        case '2':
            logs.write(f'{time} - Выбрано изменить телефон контакта!\n')
            change_phone = input('Введите измененный номер телефона: ')
            logs.write(f'{time} - Введен измененный телефон контакта {name}!\n')
            lst = []
            with open(path, 'r') as db:
                reader = csv.reader(db, delimiter=',')
                for row in reader:
                    lst.append(row)
            for i in lst:
                if name in i:
                    i[1] = change_phone
                    break
            with open(path, 'w') as db:
                writer = csv.writer(db, delimiter=',')
                writer.writerows(lst)
                logs.write(f'{time} - Телефон контакта {name} изменен!\n')
                logs.close()
                print('Номер телефона контакта изменен!')
        case _:
            print('Такого выбора нет!')

def show_all():
    logs = open(path_logs, 'a')
    logs.write(f'{time} - Нажата кнопка "Показать все контакты"!\n')
    with open(path, 'r', newline='') as db:
        reader = csv.reader(db, delimiter=',')
        for row in reader:
            print(*row)
    logs.write(f'{time} - Показаны все контакты!\n')
    logs.close()
    print('Все ваши контакты!')
