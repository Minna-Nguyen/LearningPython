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
