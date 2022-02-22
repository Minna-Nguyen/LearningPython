from validation import *
def is_name (name):
    name_regex = "[A-ZÖÄÅ][a-zäöå]+"
    # Ala-Möyhy
    name_with_dashes_regex = "[A-ZÖÄÅ][a-zäöå]+\-[A-ZÖÄÅ][a-zäöå]+"
    regex = f"^({name_regex}|{name_with_dashes_regex}) ({name_regex}|{name_with_dashes_regex})$"
    return bool(re.search(regex, name))

def ask_name (name_input):
    name_format_valid = True
    # kysy käyttäjältä nimisyötettä uudestaan niin kauan kun se ei ole Etunimi Sukunimi muodossa
    while name_format_valid:
        if is_name(name_input):
            name_format_valid = False
            return name_input
        else:
            print("Your given name must be in Firstname Lastname format")
            name_input = input("Give name: ")
        
def ask_email(email_input):
    valid_email = True
    while valid_email:
        if is_email(email_input) == True:
            valid_email = False
            return email_input
        else:
            print("Invalid email.")
            email_input = input("Give email: ")

def ask_id(id_input):
    valid_id = True
    while valid_id:
        if is_personal_id(id_input) == True:
            valid_id = False
            return id_input
        else:
            print("Invalid personal id.")
            id_input = input("Give personal id: ")

def ask_date(date_input):
    valid_date = True
    while valid_date:
        if is_date(date_input) == True:
            valid_date = False
            return date_input
        else:
            print("Invalid date. Date must be in YYYY-MM-DD form")
            date_input = input("Give personal id: ")
            
# main code, gather data of user info    
def ask_person():
    name = ask_name(input("Give name:"))
    email = ask_email(input("Give email: "))
    id = ask_id(input("Give personal id: "))
    date = ask_date(input("Give start date of work: "))

    data = {'Name': name, 'Email': email, 'Personal id': id, 'Date': date}
    return data
   
print(ask_person())