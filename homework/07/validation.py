import re
"""
Module that contains name format related functions.
"""
def is_name(name):
    """ Checks if the given name is in name format.
    Parameters
    ----------
    name: 'String'
        The value is used for testing, if it's aligns with the name format.
    Return
    ------
    value: 'boolean'
        If the given name parameter is valid, it will return True, else it will return False.
    """
    
    # contain at least two characters that are not digit
    name_regex = "[A-ZÖÄÅ][a-zäöå]{1,}"
    name_with_dashes_regex = "[A-ZÖÄÅ][a-zäöå]+\-[A-ZÖÄÅ][a-zäöå]+"
    regex = f"^({name_regex}|{name_with_dashes_regex})$"
    return bool(re.search(regex, name))