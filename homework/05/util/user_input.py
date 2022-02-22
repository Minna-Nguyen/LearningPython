from util.validation import *
"""
Module that contains name format related functions.
"""
def is_name (name):
    """ Checks if the given name is in name format and if the given name is case sensitive or not.
    Parameters
    ----------
    name: 'String'
        The value is used for testing, if it's aligns with the name format.

    ignore_case: 'boolean'
        Option if user wants to test names case sensitivity.
        
    Return
    ------
    value: 'boolean'
        If the given name parameter is valid, it will return True, else it will return False.
    """
    name_regex = "[A-ZÖÄÅ][a-zäöå]+"
    # Ala-Möyhy
    name_with_dashes_regex = "[A-ZÖÄÅ][a-zäöå]+\-[A-ZÖÄÅ][a-zäöå]+"
    regex = f"^({name_regex}|{name_with_dashes_regex}) ({name_regex}|{name_with_dashes_regex})$"
    return bool(re.search(regex, name))

"""
This module will let get an input. It will then validate the input. If given input is valid, it will return the name.
"""
def ask_name (name_input):
    """Funtion checks if the input is valid. If the given input is invalid, it will ask to get a valid input. 
    It will do this so long until a valid input is given.

    Parameter
    ---------
    name_input: 'String'
        This is the string that will be checked.
    
    Return
    ------
    value: 'String'
        Returns a valid name.
    """
    name_format_valid = True
    # kysy käyttäjältä nimisyötettä uudestaan niin kauan kun se ei ole Etunimi Sukunimi muodossa
    while name_format_valid:
        if is_name(name_input):
            name_format_valid = False
            return name_input
        else:
            print("Your given name must be in Firstname Lastname format")
            name_input = input("Give name: ")

"""
This module will let get an input. It will then validate the input. If given input is valid, it will return the email.
"""        
def ask_email(email_input):
    """Funtion checks if the input is valid. If the given input is invalid, it will ask to get a valid input. 
    It will do this so long until a valid input is given.

    Parameter
    ---------
    email_input: 'String'
        This is the string that will be checked.
    
    Return
    ------
    value: 'String'
        Returns a valid email.
    """
    valid_email = True
    while valid_email:
        if is_email(email_input) == True:
            valid_email = False
            return email_input
        else:
            print("Invalid email.")
            email_input = input("Give email: ")
"""
This module will let get an input. It will then validate the input. If given input is valid, it will return the personal id.
"""  
def ask_id(id_input):
    """Funtion checks if the input is valid. If the given input is invalid, it will ask to get a valid input. 
    It will do this so long until a valid input is given.

    Parameter
    ---------
    id_input: 'String'
        This is the string that will be checked.
    
    Return
    ------
    value: 'String'
        Returns a valid personal id.
    """
    valid_id = True
    while valid_id:
        if is_personal_id(id_input) == True:
            valid_id = False
            return id_input
        else:
            print("Invalid personal id.")
            id_input = input("Give personal id: ")
"""
This module will let get an input. It will then validate the input. If given input is valid, it will return the date.
"""  
def ask_date(date_input):
    """Funtion checks if the input is valid. If the given input is invalid, it will ask to get a valid input. 
    It will do this so long until a valid input is given.

    Parameter
    ---------
    date_input: 'String'
        This is the string that will be checked.
    
    Return
    ------
    value: 'String'
        Returns a valid date.
    """
    valid_date = True
    while valid_date:
        if is_date(date_input) == True:
            valid_date = False
            return date_input
        else:
            print("Invalid date. Date must be in YYYY-MM-DD form")
            date_input = input("Give personal id: ")
"""
Module goes through a list and the user is given the chance to modify the list.
"""
def ask(menu):
    """This funtion gets a list as an argument and will display the output.
    Parameters
    ----------
    menu: 'data type dictionary'
        Argument is a data type list.
    """
# Display the menu options
    for menu_option in menu:
        print(f"{menu_option}: {menu[menu_option]}")
"""
This module asks one numeric value.
"""
def ask_int(message, min, max):
    """This function asks an int value and will return a valid int value.
    Parameters
    ----------
    message: 'int'
        This value is an int type. Value must be within 'min' - 'max' parameters
    min: 'int'
        Minimum int value
    max: 'int'
        Maximum int value
    
    Return
    ------
    value: 'int'
        Returns a valid int value
    """
    while True:
        while True:
            try:
                # katsotaan onko käyttäjän syöte int tyyppi
                # olettaen että syöte on alustavasti numero, joka oli 'String'
                # int() muuttaa int tyypiksi
                message = int(message)
                break
            except:
                message = input("Try again, give a number: ")

        if message < min or message > max:
            print(f"Your choice must be between {min} - {max}")
            message = int(input())
        else:
            return message - 1
            
"""
This module will gather information from the end user such as: name, email address, personal id and date.
"""
def ask_person():
    """This function will ask the end user to input information such as name, email address, personal id and date.
    When all the data(valid) are gathered, it will input those into a 'dictionary' type database.
    
    Parameter
    ---------
    none

    Return
    ------
    value: 'dictionary'
        Returns a dictionary database.
    """
    name = ask_name(input("Give name:"))
    email = ask_email(input("Give email: "))
    id = ask_id(input("Give personal id: "))
    date = ask_date(input("Give start date of work: "))

    data = {'Name': name, 'Email': email, 'Personal id': id, 'Date': date}
    return data
   