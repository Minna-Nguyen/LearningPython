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

"""
A module that validates the player input.
"""
def validate_player_input(is_letter):
    """Function will go check if the player input is just one letter. It will ask the player a new input again if the input wasn't one in length or a string type.
    Parameter
    ---------
    is_letter: 'String'
        User input that is a string type. This will be validated if it is just one letter or not.
    Return
    ------
    value: 'String'
        Returns a validated string that is a one letter. 
    """
    while True:
            valid_input = "^[a-zA-Z]{1}$"
            regex = bool(re.search(valid_input, is_letter))
            if regex:
                return is_letter
            else:
                is_letter = input("Your guess cannot be longer than one letter or a non-alphabetic character: ")


"""
Module that contains function required for the hangman game.
"""
def hangman_game():
    hangman_ascii = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O<  |
 /|\  |
 / \  |
      |
=========''']
    # Open and read the text file.
    words = read_database()
    # split the text file into substrings by enter (\n). The split() funtion will create a list where the element is the words.
    words = words.split("\n")
    # print(f'This is the whole list:\n {words}')
    # print(f'And this the third word: {words[2]}')

    # print("------")

    random_word = random.randint(0, len(words)-1)


    keep_gessing = True
    
    guesses = set()
    secret_word = list()
    incorrect_guesses = set()

    for i in range(0, len(words[random_word])):
        secret_word.append("_")
    #display the hangman starting graph
    print(hangman_ascii[0])
    # display the dashes
    print("".join(secret_word), end="\n\n")
   
    while keep_gessing:
        player_input = input("Your guess: ")
        validate_player_input(player_input)
        
        print()
        # ["m","m","m","m","m"]
        # ["0","1","2","3","4"]
        if player_input in words[random_word]:
            for index in range(0, len(words[random_word])):
                if player_input == words[random_word][index]:
                    secret_word[index] = player_input
        else:
            incorrect_guesses.add(player_input)
        # display secret word so far
        print("".join(secret_word))

        # display the hangman steps when there is a wrong answer from the player
        if len(incorrect_guesses) == 1:
            print(hangman_ascii[1])
        elif len(incorrect_guesses) == 2:
            print(hangman_ascii[2])
        elif len(incorrect_guesses) == 3:
            print(hangman_ascii[3])
        elif len(incorrect_guesses) == 4:
            print(hangman_ascii[4]) 
        elif len(incorrect_guesses) == 5:
            print(hangman_ascii[5])
        elif len(incorrect_guesses) == 6:
            print(hangman_ascii[6])
            print("You lost!")
            keep_gessing = False
        
        
        # if the player was able to guess the word correctly, game end
        if "".join(secret_word) == words[random_word]:
            keep_gessing = False
            print("WINNIIIING!")
        # display only when there is some element in the set()
        if len(incorrect_guesses) != 0:
            print("Misses: ", incorrect_guesses)

hangman_game()
