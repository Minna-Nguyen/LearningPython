from string_helper import csv_to_list
from validation import is_name

"""
Module contains a function that will read a txt file.
"""
def read_database():
    """Function that read the txt file.
    Return
    ------
    value: 'String'
        Returns the file as a string.
    """
    #string type
    f = open("database.txt", "r")
    return f.read()


"""
Module that will save the given firstname lastname to the file called  'database.txt'
"""
def save_to_database(fname,lname):
    """This function validates if the given string is in name format. It will then save the valid name to the database.txt
    Parameters
    ----------
    fname: 'String'
        A string that will be validated if it's a valid name form or not.
    name: 'String'
        A string that will be validated if it's a valid name form or not.
    """
    #avaa ton filen
    database = read_database()
    #lähettää ton tekstitiedoston tohon funktioon, joka jaottelee näitä osia
    two_dim_database = csv_to_list(database)
    # if is_name(f"{fname} {lname}") == True:
    # avaa tiedoston ja lisää sitten nimen tiedostoon käyttäen 'append' tapaa
    open_file = open("database.txt", "a")
    open_file.write(f"{len(two_dim_database)},{fname},{lname}\n")
    open_file.close()

# print(save_to_database("Test","Hii"))