import csv

path = '/Users/ivanfedulov/Desktop/python ed/project_tel_book/db.csv'

def add_contact():
    name = input('\nВведите имя контакта: ')
    phone = input(f'Введите номер телефона контакта {name}: ')
    list_data = [name, phone]
    with open(path, 'a', newline='') as db:
        writer = csv.writer(db, delimiter=';')
        writer.writerow(list_data)


def find_contact():
    find_name = input('\nВведите имя для поиска контакта: ')
    with open(path, 'r', newline='') as db:
        reader = csv.reader(db, delimiter=';')
        for row in reader:
            if find_name == row[0]:
                print(*row)


def del_contact():
    name = input('\nВведите имя контакта, который хотите удалить: ')
    lst = []
    with open(path, 'r') as db:
        reader = csv.reader(db, delimiter=';')
        for row in reader:
            lst.append(row)
    for i in lst:
        if name in i:
            lst.remove(i)
            break
    with open(path, 'w') as db:
        writer = csv.writer(db, delimiter=';')
        writer.writerows(lst)


def change_contact():
    name = input('\nВведите имя контакта, который хотите изменить: ')
    choice = input('Что вы хотите изменить?\n1. Имя\n2. Номер телефона\n :')
    match choice:
        case '1':
            change_name = input('Введите измененное имя: ')
            lst = []
            with open(path, 'r') as db:
                reader = csv.reader(db, delimiter=';')
                for row in reader:
                    lst.append(row)
            for i in lst:
                if name in i:
                    i[0] = change_name
                    break
            with open(path, 'w') as db:
                writer = csv.writer(db, delimiter=';')
                writer.writerows(lst)
        case '2':
            change_phone = input('Введите измененный номер телефона: ')
            lst = []
            with open(path, 'r') as db:
                reader = csv.reader(db, delimiter=';')
                for row in reader:
                    lst.append(row)
            for i in lst:
                if name in i:
                    i[1] = change_phone
                    break
            with open(path, 'w') as db:
                writer = csv.writer(db, delimiter=';')
                writer.writerows(lst)
        case _:
            print('Такого выбора нет!')


def show_all():
    with open(path, 'r', newline='') as db:
        reader = csv.reader(db, delimiter=';')
        for row in reader:
            print(*row)
