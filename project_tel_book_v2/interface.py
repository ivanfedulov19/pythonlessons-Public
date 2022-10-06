import tkinter as tk
import commands
import datetime

def start_interface():  
    time = datetime.datetime.now().replace(microsecond=0)
    logs = open('/Users/ivanfedulov/Desktop/python ed/project_tel_book_v2/logs.txt', 'a')
    logs.write(f'{time} - Приложение запущено!\n')
    logs.close()
    win = tk.Tk()
    win.geometry('293x242+1400+100')
    win.title('Моя телефонная книга')

    label = tk.Label(win, text='Выберите одну из операций', font=('Arial',20,'bold')).grid(row=0, column=0,columnspan=2)
    button_0 = tk.Button(win,text='Импортировать старые контакты', command=commands.import_contacts).grid(row=1,column=0, stick = 'wens', columnspan=2)
    button_1 = tk.Button(win,text='Создать контакт', command=commands.create_contact).grid(row=2,column=0, stick = 'wens')
    button_2 = tk.Button(win,text='Найти контакт', command=commands.find_contact).grid(row=2,column=1,stick = 'wens')
    button_3 = tk.Button(win,text='Изменить контакт', command=commands.change_contact).grid(row=3,column=0, stick = 'wens')
    button_4 = tk.Button(win,text='Удалить контакт', command=commands.del_contact).grid(row=3,column=1, stick = 'wens')
    button_5 = tk.Button(win,text='Показать все контакты', command=commands.show_all).grid(row=4,column=0, columnspan=2, stick = 'wens')

    win.rowconfigure(0,minsize=40)
    win.rowconfigure(1,minsize=50)
    win.rowconfigure(2,minsize=50)
    win.rowconfigure(3,minsize=50)
    win.rowconfigure(4,minsize=50)

    win.mainloop()
