def is_name(name):
    name_format = False
    # all the below ones are to check the validness of the name format!
    only_letters = False
    is_space = False
    capital_first_letter = False
    capital_last_letter = False
    name_first_length = False
    name_last_length = False
    space_before_or_after = False

    # divide the name into two part: fist and last name!
    full_name = name.split()

    # checks if name has 2 words as first and last name.
    # If it's in form 'first name' and 'last name', then proceed to check the name format validness
    if len(full_name) == 2:
        # isalpha() => only alphabetics in string
        if full_name[0].isalpha() and full_name[1].isalpha():
            name_format = True    
        # check if it has space
        # for character in name: 
        #     if character == " ":
        #         is_space = True

        # def format_ok():
        #     if (first_name != first_name + " " or first_name != " " + first_name) or (last_name != " " or last_name != " " + last_name):
        #         # space_before_or_after = True
        #         # retruns False
        #         return name_format 
        

        # check if first name starts with capital letters and ends with lowercase letters.
        if full_name[0].istitle() and full_name[1].istitle():
            name_format = True
        # check if last name starts with capital letter and ends with lowercase letters.
        # istitle() check first uppercase letter and the rest lowercase.
        # if last_name.istitle():
        #     capital_last_letter = True

        # name has at least 2 characters
        # len() returns amount of characters are in the string (or variable in array)
        # if len(first_name) >= 2:
        #     name_first_length = True
            
        # # name has at least 2 characters
        # if len(last_name) >= 2:
        #     name_last_length = True
        
        # # #check name format is valid
        # if only_letters == True and is_space == True and capital_first_letter == True and capital_last_letter == True and name_first_length == True and name_last_length == True:
        #     name_format = True
        # else:
        #     name_format = False
            if name_format:
                return name_format
            else:
                return name_format
    else:
        return name_format
            

# print(is_name("Hello World"))
# print(is_name("ille Ugh"))
# print(is_name("Minna"))
# print(is_name("minna"))
# print(is_name("123"))