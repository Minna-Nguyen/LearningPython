import re
"""
Module that contains name format related functions.
"""
def is_name(name):
    """ Checks if the given name is in name format and if the given name is case sensitive or not.
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
    ok_regex = f"^({name_regex}) ({name_regex})$"
    return bool(re.search(ok_regex, name))

print(is_name("Te Tee"))