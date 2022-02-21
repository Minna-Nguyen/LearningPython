from cgi import test
import re
"""
Module that validates the given date.
"""
def is_date(date):
    """A function that validates the date. Given date must be in ISO format: 'YYYY-MM-DD'. 
    For example '2021-06-28'.

    Parameter
    ---------
        date: 'String'
            Given date format is a string in a from 'YYYY-MM-DD'.
    
    Exception
    ---------
        - value must be a string
    
    Return
    ------
        value: 'bool'
            If given date format is in correct form, returns True else returns False.
    """
    if not isinstance(date, str):
        raise Exception("Given argument must be a string")
    date_ok = ""
    
    for character in date:
        if character == "-":
            check_valid_numbers = date.split("-")
            year = check_valid_numbers[0]
            months = check_valid_numbers[1]
            dates = check_valid_numbers[2]
            # check if the year is '-XX' form
            for char in year:
                if char == "-":
                    return False
                else:
                    if int(year) >= 0 and (int(months) >= 1 and int(months) <= 12) and (int(dates) >= 1 and int(dates) <= 31):
                        date_ok = f"{year}-{months}-{dates}"
                    
                        match_object = re.search("^[0-9]{4}\-.[0-9]\-.[0-9]$", date_ok)

                        return bool(match_object)
                        
"""
Module that validates the given email.
"""
def is_email(email):
    """A function that validates the given email address form.

    Parameter
    ---------
        email: 'String'
            Given string will be tested if it's proper email address or not.
    
    Exception
    ---------
        - value must be a string
    
    Return
    ------
        value: 'bool'
            If given email format is in correct form, returns True else returns False.
    """
    if not isinstance(email, str):
        raise Exception("Given argument must be a string")
    # minna-minna@email.com | minna.minna@email.com | minna_minna@email.com
    regex_with_char = "^([a-z0-9]+[._-]{1})+([a-z0-9]{1,})+@+[a-z]+[.][a-z]{2,3}$"
    # minna@email.com
    regex_only_name = "^([a-z0-9])+@+[a-z]+[.][a-z]{2,3}$"

    regex = f"(^{regex_with_char})|(^{regex_only_name})$"
    return bool(re.search(regex, email))

def is_personal_id(id):
    pp = "^([1-2][0-9]|0[1-9]|3[0-1])"
    kk = "(1[0-2]|0[1-9])"
    vv = "([0-9][0-9])"
    a_minus_plus = "[+-A]"
    nnn = "(00[2-9]|0[1-9][0-9]|[1-8][0-9][0-9])"
    id_last_part = "[0123456789ABCDEFHJKLMNPRSTUVWXY]$"
    """
    A module that calculates the last id part of a personal id
    """
    # def tunnusmerkki (char):
    """Given personal id, this function will calculate and return the last id part.
    Parameter
    ---------
        char: 'String'
            A string that is either '+', '-' or 'A'. This will be used to know where to split the personal id digits into two part: 
            a six digit and a three digit. These will be joined into one nine-digit long int. 
            The gotten nine digit int will be further used to calculate what the last id part will. It's either one of 0-9 or one of the 'ABCDEFHJKLMNPRSTUVWXY' letter.
    Return
    ------
        value: 'String'
            After the modulus calculation, the function will return the corresponding value.
    """
    #     breakmark = id.split(char)
    #     merkit ="0123456789ABCDEFHJKLMNPRSTUVWXY"
    #     # loop through the id.split, join them into one string and convert to int type
    #     nine_digit = ""
    #     for i in breakmark:
    #         nine_digit += i
    #     nine_digit_converted = int(nine_digit)
            # %-merkki w3school mukaan on itseisarvoa varten
    #     math = nine_digit_converted % 31
    #     # goes trough the merkit string and indicates what last 
    #     vika = merkit[math]
    #     return vika

    # minus_mark_id_last_part = (tunnusmerkki("-"))
    # plus_mark_id_last_part = (tunnusmerkki("+"))
    # a_mark_id_last_part = (tunnusmerkki("A"))
    # regex_1800 = f"{pp}{kk}{vv}{nnn_plus}{plus_mark_id_last_part}"
    # regex_1900 = f"{pp}{kk}{vv}{nnn_miinus}{minus_mark_id_last_part}"
    # regex_2000 = f"{pp}{kk}{vv}{nnn_a}{a_mark_id_last_part}"
    regex = f"{pp}{kk}{vv}{a_minus_plus}{nnn}{id_last_part}"
    return bool(re.search(regex, id))
