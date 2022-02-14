from user_input import  ask_name, ask, ask_int
from string_helper import list_to_str

# a list containing names
database = ["Gucci Good", "Hannah Smith", "Aku Ankka", "Andy Andyyy", "Iines Ankka", "Mikki Hiiri", "Hessu Hopo", "Minni Hiiri", "Roope Ankka", "Pelle Peloton", "Taavi Ankka", "Hannu Hanhi"]
# a dictionary containing menu options
menu = {1: "Add", 2: "Insert", 3: "Remove", 4: "Clear", 0: "Exit"}

while True:
    # jos database ei ole tyhjä, jatka tätä while -looppia kunnes 
    # käyttäjä haluaa lopettaa tän '0' menu option
    print()
    if database != []:
        print(f"Database:\n{list_to_str(my_list=database)}")
    else:
        print("Empty string, just like my head.")
        
    # display menu options
    print("Menu:")
    ask(menu)
    print()
    # asking about the menu options action
    user_input_menu = ask_int(input("Your choice: "), 0, len(menu)-1)
    print()

    # add new name
    if user_input_menu == 0:
        database.append(ask_name(input("Give name: ")))
    # insert new name at what location
    elif user_input_menu == 1:
        user_input_db = ask_int(input("Where to insert: "), 1, len(database))
        new_name = ask_name(input("Give name: "))
        database.insert(user_input_db, new_name)
    # remove name at some location
    elif user_input_menu == 2:
        user_input_db = ask_int(input("What to remove: "), 1, len(database))
        database.pop(user_input_db)
    # clear the db
    elif user_input_menu == 3:
        database.clear()
        print("Database cleared.")
    else:
        break
