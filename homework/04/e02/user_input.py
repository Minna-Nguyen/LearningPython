from string_helper import is_name
"""
This module asks one numeric value.
"""
# function that returns an int between range a - b
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
A module that will checks the user's given name. It will then validate if the name is in correct name format or not.
"""

def ask_name(name_message):
    """This function checks will keep asking the user's name input until the name format is Firstname Lastname format
    Parameters
    ----------
    message: 'String'
        A string value is given to this as an argument. 
    
    Returns
    -------
    value: 'String'
        Processed string will be returned if the name is in correct name format.
    """
    name_format_valid = True
    # kysy käyttäjältä nimisyötettä uudestaan niin kauan kun se ei ole Etunimi Sukunimi muodossa
    while name_format_valid:
        if is_name(name_message, ignore_case=False):
            name_format_valid = False
            return name_message
        else:
            print("Your given name must be in Firstname Lastname format")
            ask_name_again = input("Give name: ")
            check_valid_name = is_name(ask_name_again, ignore_case=False)
            if check_valid_name == True:
                name_format_valid = False
                return ask_name_again

"""
Module goes through a list and user is given the chance to modify the list.
"""
def ask(choices):
    """This funtion gets a list as an argument and will display the output.
    Parameters
    ----------
        choices: 'data type dictionary'
            Argument is a data type list.
    """
# Display the menu options
    for menu_option in choices:
        print(f"{menu_option}: {choices[menu_option]}")