from util.user_input import ask_int
from util.user_input import ask
from util.user_input import ask_person

def main():
    menu = {1: "Add", 0: "Exit"}

    employees = []

    continue_loop = True
    while continue_loop:
        print()
        # display menu options
        print("Menu:")
        ask(menu=menu)
        print()
        # asking about the menu options action
        user_input = ask_int(input("Your choice: "), 0, len(menu)-1)
        print()

        # add new name
        if user_input == 0:
            employee = ask_person()
            print()
            employees.append(employee)
            print(employees)
        else:
            continue_loop = False

main()