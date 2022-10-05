import gui
import commands

def start_app():
    user_choice = input(gui.operations())
    match user_choice:
        case '1':
            commands.add_contact()
        case '2':
            commands.find_contact()
        case '3':
            commands.change_contact()
        case '4':
            commands.del_contact()
        case '5':
            commands.show_all()
        case _:
            print("Такой операции не существует!")
