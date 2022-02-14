import re
"""
Module that contains name format related functions.
"""
def is_name(name, ignore_case=False):
    """ Checks if the given name is in name format and if the given name is case sensitive or not.
    Parameters
    -------------
    name: 'String'
        The value is used for testing, if it's aligns with the name format.

    ignore_case: 'boolean'
        Option if user wants to test names case sensitivity.
        
    Returns
    -------
    value: 'boolean'
        If the given name parameter is valid, it will return True, else it will return False.
    """
    # Matti
    name_regex = "[A-ZÖÄÅ][a-zäöå]+"

    # Ala-Möyhy
    name_with_dashes_regex = "[A-ZÖÄÅ][a-zäöå]+\-[A-ZÖÄÅ][a-zäöå]+"

    regex = f"^({name_regex}|{name_with_dashes_regex}) ({name_regex}|{name_with_dashes_regex})$"
    # if ignore_case = True, given  name string is correct name format else it's false
    return bool(re.search(regex, name, re.IGNORECASE)) if ignore_case else bool(re.search(regex, name))

"""
Module that converts list in to string
"""
def list_to_str(my_list):
    """Functions that will convert the list to a string
    Parameter
    ---------
    my_list: 'list'
        Database list

    Exceptions
    ----------
    - If argument is not a list
    - If argument list size is 0
    - If argument list does not contain strings
    - If argument list item is string but string length is 0

    Return
    ------
    value: 'String'
        List of databases names.
    """

    return_str = ""
    if len(my_list) == 0:
        raise Exception("List size cannot be 0.")
    if not isinstance(my_list, list):
        raise Exception("Argument list is not a list.")

    # print -> index: "string"
    for index in range(0, len(my_list)):
        if not isinstance(my_list[index], str):
            raise Exception("Argument list does not contain any string.")
        if my_list[index] == "":
            raise Exception("Argument list item is string but string length is 0.")
        return_str += f"{index + 1}: {my_list[index]}\n" 

    return return_str
