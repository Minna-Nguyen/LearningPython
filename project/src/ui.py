import re
"""
A module that validates the player input.
"""
def validate_player_input(is_letter):
    """Function will go check if the player input is just one letter.
    Parameter
    ---------
    is_letter: 'String'
        User input that is a string type. This will be validated if it is just one letter or not.
    Return
    ------
    value: 'bool'
        Returns True if valid string, else False. 
    """
    valid_input = "^[a-zA-Z]{1}$"
    regex = bool(re.search(valid_input, is_letter))
    return regex

"""
A module that ask the player name. It also validates the given name and returns a valid name.
"""
def ask_name(name):
    """Function will validate player name input and returns the valid name
    Parameter
    ---------
    name: 'String'
        This string will be validated.
    Return
    ------
    value: 'String'
        Retruns the validated name string.
    """
    # name starts with a capital letter, and name length is at least 2 letters long
    valid_input = "^[A-Z][a-z]{1,}$"
    regex = bool(re.search(valid_input, name))
    return regex