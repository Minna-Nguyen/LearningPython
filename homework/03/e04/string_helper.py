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
        If the given name parameter is valid, it will return True, else it will return False.
    """
    name_format = False
    # all the below ones are to check the validness of the name format!
    only_letters = False
    is_space = False
    capital_first_letter = False
    capital_last_letter = False
    name_first_length = False
    name_last_length = False

    # divide the name into two part: fist and last name!
    full_name = name.split()

    # checks if name has 2 words as first and last name. 
    # If it's in form 'first name' and 'last name', then proceed to check the name format validness
    if len(full_name) == 2:
        first_name = full_name[0]
        last_name = full_name[1]
        
        # isalpha() => only alphabetics in string
        if first_name.isalpha() and last_name.isalpha():
            only_letters = True
        
        # check if it has space
        for character in name: 
            if character == " ":
                is_space = True


        if ignore_case == True:
            capital_first_letter = True
            capital_last_letter = True
        else:
            # check if first name starts with capital letters and ends with lowercase letters.
            # istitle() check first uppercase letter and the rest lowercase.
            if first_name.istitle():
                capital_first_letter = True

            # check if last name starts with capital letter and ends with lowercase letters.
            # istitle() check first uppercase letter and the rest lowercase.
            if last_name.istitle():
                capital_last_letter = True

        # name has at least 2 characters
        # len() returns amount of characters are in the string (or variable in array)
        if len(first_name) >= 2:
            name_first_length = True
            
        # name has at least 2 characters
        if len(last_name) >= 2:
            name_last_length = True
        
        # #check name format is valid
        if only_letters == True and is_space == True and capital_first_letter == True and capital_last_letter == True and name_first_length == True and name_last_length == True:
            name_format = True
        else:
            name_format = False
        
    return name_format

# print(is_name("Hello World", ignore_case=False))
# print(is_name("ille Ugh", True))
# print(is_name("ille uugh", ignore_case=True))
# print(is_name("Minna"))
# print(is_name("123"))