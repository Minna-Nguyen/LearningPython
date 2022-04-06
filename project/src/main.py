import random
import re

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
    f = open("words.txt", "r")
    return f.read()


def validate_player_input(is_letter):

     while True:
            valid_input = "^[a-z]{1}$"
            regex = bool(re.search(valid_input, is_letter))
            if regex:
                # break
                return is_letter
            else:
                is_letter = input("Your guess cannot be longer than one letter or a non-alphabetic character: ")


"""
Module that contains function required for the hangman game.
"""
def hangman_game():

    # Open and read the text file.
    words = read_database()
    # split the text file into substrings by enter (\n). The split() funtion will create a list where the element is the words.
    words = words.split("\n")
    # print(f'This is the whole list:\n {words}')
    # print(f'And this the third word: {words[2]}')

    # print("------")

    random_word = random.randint(0, len(words)-1)

    keep_gessing = True
    guesses = ""
    false_guesses = ""

    dashes = "_" * len(words[0])
    print(dashes)
   
    while keep_gessing:
        secret_word = ""
        # Checker keeps count on the length of the secret word. 
        checker = 0

        player_input = input("Your guess: ")
        print(validate_player_input(player_input))

        # validating the input
        # while True:
        #     valid_input = "^[a-z]{1}$"
        #     regex = bool(re.search(valid_input, player_input))
        #     if regex:
        #         break
        #     else:
        #         player_input = input("Your guess cannot be longer than one letter or a non-alphabetic character: ")

            # else:
                


            # if len(player_input) != 1:
            #     player_input = input("You must enter one letter: ")
            # elif type(player_input) != str():
            #     player_input = input("Your guess must be a letter: ")
            # # elif isinstance(player_input, str):
            #     print("Please give a letter.")
            #     break
            # else:
            #     break
        guesses += player_input

        print()
        # go through what letters the word contains
        for letter in words[0]:
            checker += 1
            # checking guesses of the player
            for guess_letter in guesses:
                if guess_letter == letter:
                    secret_word += letter
                    break
            
            if len(secret_word) != checker:
                secret_word += "_"
        # if the player was able to guess the word correctly, game end
        if secret_word == words[0]:
            keep_gessing = False
    
        # board
        print(secret_word)

        # emt data??
        # print("False: ", false_guesses)

hangman_game()



# x = "123"
# y = "1"
# z =" aöldfkjasöldfjkasldökf"
# i = "o"
# valid = "^[a-z]{1}$"

# while True:
#     regex = bool(re.search(valid, i))
#     print("Hello?")
#     if regex:
#         print("toimiiko")
#         break
# print(regex)
    

# print(bool(re.search(valid, x)))
# print(bool(re.search(valid, y)))
# print(bool(re.search(valid, z)))