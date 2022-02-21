from validation import *
def is_name (name):
    name_regex = "[A-ZÖÄÅ][a-zäöå]+"
    # Ala-Möyhy
    name_with_dashes_regex = "[A-ZÖÄÅ][a-zäöå]+\-[A-ZÖÄÅ][a-zäöå]+"
    regex = f"^({name_regex}|{name_with_dashes_regex}) ({name_regex}|{name_with_dashes_regex})$"
    return bool(re.search(regex, name))
def ask_name (name):
    valid = True
    while valid:
        if is_name(name) == True:
            valid = False
            return name
        else:
            name = is_name(input("Give name: "))
            print("Name must be Firstname Lastname format")
            if name == True:
                valid = False
        
def ask_person():


    is_valid = True
    while is_valid:
        print("Give name: ", end="")
        name = is_name(input())
        if name == True:
            break
        else:
            print("Name must be Firstname Lastname")

        print("Give email: ", end="")
    
    while True:
        print("Give personal id: ", end="")
        personal_id = is_personal_id(input())
        if personal_id == True:
            break
        else:
            print("Invalid personal id")
    # data = {'Email': email}
   
print(ask_person())


#  name_regex = "[A-ZÖÄÅ][a-zäöå]+"

#     # Ala-Möyhy
#     name_with_dashes_regex = "[A-ZÖÄÅ][a-zäöå]+\-[A-ZÖÄÅ][a-zäöå]+"

#     regex = f"^({name_regex}|{name_with_dashes_regex}) ({name_regex}|{name_with_dashes_regex})$")