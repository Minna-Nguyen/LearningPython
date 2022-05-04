import os
from operator import itemgetter
import random
import time
import re
"""
A module that validates the player input.
"""
def validate_player_input(is_letter):
    """Function will go check if the player input is just one letter.
    Parameter
    ---------
    is_letter: 'String'
        User input that is a string type. This will be validated if it is just one letter or not.
    Return
    ------
    value: 'bool'
        Returns True if valid string, else False. 
    """
    valid_input = "^[a-zA-Z]{1}$"
    regex = bool(re.search(valid_input, is_letter))
    return regex

"""
A module that ask the player name. It also validates the given name and returns a valid name.
"""
def ask_name(name):
    """Function will validate player name input and returns the valid name
    Parameter
    ---------
    name: 'String'
        This string will be validated.
    Return
    ------
    value: 'String'
        Retruns the validated name string.
    """
    # name starts with a capital letter, and name length is at least 2 letters long
    valid_input = "^[A-Z][a-z]{1,}$"
    regex = bool(re.search(valid_input, name))
    return regex

"""
Module contains a function that will read a txt file.
"""
def read_secret_word_database():
    """Function that read the txt file.
    Return
    ------
    value: 'String'
        Returns the file as a string.
    """
    #string type
    f = open("words.txt", "r")
    return f.read()

# """
# Module that will save the given firstname lastname to the file called  'words.txt'
# """
# def add_to_database():
#     """This function validates if the given string is in name format. It will then save the valid name to the words.txt
#     """
#     #avaa ton filen
#     database = read_secret_word_database()
#     #lähettää ton tekstitiedoston tohon funktioon, joka jaottelee näitä osia
#     # two_dim_database = csv_to_list(database)
#     # avaa tiedoston ja lisää sitten nimen tiedostoon käyttäen 'append' tapaa
#     open_file = open("words.txt", "a")
#     test = input("What word do you wish to add?: ")
#     open_file.write(f'{test}\n')
#     open_file.close()

"""
Module that will create a new text file and save player's highscore of the words. 
"""
def save_highscore_files(name, high, file):
    """This function will create new text file named after the player's name and list all the highscore of the words.
    Parameter
    ---------
    name: 'String'
        Player name will be saved into the highscore text file.
    high: 'int'
        This variable is int type, but will be converted to str type. This is the highscore (time seconds) that will be saved into the file. 
    file: 'String'
        File variable contains the 'file'.txt path.
    """
    some_file = open(f"{file}", "a")
    some_file.write(f'{name}, {high}\n')

"""
Module that will read all highscores and will display 
"""
def read_highscore():
    """Function contains logic that will read the highscore text file. It will display top 3 players' highscore. 
    """
    for file in os.listdir("..\src"):
        if file.endswith(".txt") and not file.endswith("words.txt"):
            f = open(file, "r")
            #strip() will ignore the empty line
            read = f.read().strip("\n")
            f.close()
            print(f'word: "{file[0:-4]}"') 
            # [[word], [number]], outer [] is two_dim_db
            try:
                two_dim_db = []
                for line in read.split("\n"):
                    number = []
                    first_in_two_dim_db = True
                    for l in line.split(", "):
                        word = []
                        if first_in_two_dim_db: 
                            word = l
                            first_in_two_dim_db = False
                        else:
                            word = int(l)
                        number.append(word)
                    two_dim_db.append(number)
                # sort the players acording to their time highscore. Sorted based on 'Key=itemgetter(1)', is int type. Is the same
                # as two_dim_db[i][1]. Although in the text file the order is not fastest time, here it will print the fastest time first.
                sorted_two_dim_db = sorted(two_dim_db, key=itemgetter(1))
                if len(sorted_two_dim_db) == 1:
                    print(f'{sorted_two_dim_db[0][0]}, {sorted_two_dim_db[0][1]} seconds')
                elif len(sorted_two_dim_db) == 2:
                    for i in range(0, 2):
                        print(f'{sorted_two_dim_db[i][0]}, {sorted_two_dim_db[i][1]} seconds')
                else:
                    for i in range(0, 3):
                        print(f'{sorted_two_dim_db[i][0]}, {sorted_two_dim_db[i][1]} seconds')
            except:
                print("...")
            print()

"""
Module that contains function required for the hangman game.
"""
def hangman_game():
    """This function contains the hangman gameplay logic.
    Return
    ------
    value: 'String'
        Returns the guessed word.
    """
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
    words = read_secret_word_database()
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
        # validate player letter input
        while True:
            player_input = input("Your guess: ")
            letter_ok = validate_player_input(player_input)
            if letter_ok:
                break
            else:
                print("Your guess cannot be longer than one letter or a non-alphabetic character: ")
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
            print("You lost!\n")
            keep_gessing = False
        
        # if the player was able to guess the word correctly, game end
        if "".join(secret_word) == words[random_word]:
            keep_gessing = False
            print("WINNIIIING!")
            return "".join(secret_word)

        # display 'incorrect_guesses set()' only when there is some element in the set()
        if len(incorrect_guesses) != 0:
            print("Misses: ", incorrect_guesses)
"""
A module where the main code is happening.
"""
def main():
    play = "Play"
    check = "Check highscore"
    quit_game = "End game"
    choices = [play, check, quit_game]
    game_on = True
    print("Welcome to hangman game!")


    while game_on:
        print("\n1: Play")
        print("2: Check highscore")
        print("3: End game")

        user_input = int(input("\nWhat do you want to do?\n"))
    
        if user_input != -1:
            # if choice is PLAY, ask player name and start the game
            if choices[user_input-1] == play:
                while True:
                    player_name = input("What is your name?\n")
                    check_name = ask_name(player_name)
                    if check_name:
                        break
                    else:
                        print("Your name must start with a capital letter and be at least two letters long.")
                
                starting_time = int(time.time())
                file = f"{hangman_game()}.txt"
                highscore = int(time.time()) - starting_time
                save_highscore_files(player_name, highscore, file)
                print(highscore, "seconds\n")
            
            elif choices[user_input-1] == check:
                print("\nRetrieving highscores\n")
                read_highscore()

            elif choices[user_input-1] == quit_game:
                print("Thanks for playing!")
                break
main()