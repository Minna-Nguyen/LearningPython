import random
import time
from ui import validate_player_input
from ui import ask_name
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
Module that will save the given firstname lastname to the file called  'words.txt'
"""
def add_to_database():
    """This function validates if the given string is in name format. It will then save the valid name to the words.txt
    """
    #avaa ton filen
    database = read_database()
    #lähettää ton tekstitiedoston tohon funktioon, joka jaottelee näitä osia
    # two_dim_database = csv_to_list(database)
    # avaa tiedoston ja lisää sitten nimen tiedostoon käyttäen 'append' tapaa
    open_file = open("words.txt", "a")
    test = input("What word do you wish to add?: ")
    open_file.write(f'{test}\n')
    open_file.close()

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
    random_word = random.randint(0, len(words)-1)

    keep_gessing = True
    
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
        letter_ok = validate_player_input(player_input)
        
        if letter_ok == True:
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

            # display 'incorrect_guesses set()' only when there is some element in the set()
            if len(incorrect_guesses) != 0:
                print("Misses: ", incorrect_guesses)
        else:
            print("Your guess cannot be longer than one letter or a non-alphabetic character: ")
"""
A module where the main code is happening.
"""
def main():
    print("Welcome to hangman game!\nWhat is your name?\n")
    while True:
        player_name = input()
        check_name = ask_name(player_name)
        if check_name:
            starting_time = int(time.time())
            hangman_game()
            print(int(time.time()) - starting_time, "seconds")
            break
        else:
            print("Your name must start with a capital letter and be at least two letters long.")

# add_to_database()
main()