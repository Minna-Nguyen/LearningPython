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

"""
Module that will add new word from the administrator to the file called  'words.txt'
"""
def add_to_database():
    """This function validates the word given from administrator. If it's a valid input, then add to the words.txt
    """
    database = read_secret_word_database()
    print(f"\nThis is the whole word list:\n{database}")
    secret_word_list = []
    for j in database.split("\n"):
        secret_word_list.append(j)
    word_ok = "^[a-z]{2,}$"
    while True:
        new_word = input("The word you wish to add: ")
        if bool(re.search(word_ok, new_word)):
            open_file = open("words.txt", "a")
            open_file.write(f'{new_word}\n')
            open_file.close()
            break
        else:
            print("Your given word cannot contain anything else but alphabets. Word must be at least 2 letters long. Do not use capitalized words.")
    # create new .txt file from the new given word
    new = open(f'{new_word}.txt', 'a')    
    new.close()
"""
Module that will remove a word from the administrator to the file called  'words.txt'
"""
def remove_form_database():
    """This function validates the word given from administrator. If it's a valid input, then remove it form the words.txt. It will also delete the file from the directory.
    """
    database = read_secret_word_database()
    print(f"\nThis is the whole word list:\n{database}")
    secret_word_list = []
    for j in database.split("\n"):
        secret_word_list.append(j)
    # remove() will remove input (str) from the secret_word_list!
    remove_word = input("The word you wish to remove: ")
    secret_word_list.remove(remove_word)
    # open the file first, then delete the word and save to the words.txt file
    f = open("words.txt", "w")
    # check if the secret_word_list contains any '' element
    for word in secret_word_list:
        if word == "":
            secret_word_list.remove("")
        else:
            f.write(f'{word}\n')
    f.close()
    # delete the file too
    for file in os.listdir("..\src"):
        os.remove(f'{remove_word}.txt')



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
Module that contains function for log in.
"""
def log_in():
    """Function validates the player. If the credentials (admin/admin) are correct, welcome the administrator.
    Return
    ------
    value: 'bool'
        If the log in is correct then return True, else return False.
    """
    print("\nYou need to log in to use this feature.\n")
    count = 0
    while True:
            username = input("Give username: ")
            password = input("Give password: ")
            print()
            #log in tries, if tries sum to 3 -> access denied
            count+=1
            if count >= 3:
                print("You have tried too many times. Access denied!")
                return False
            elif count == 1 or count == 2:
                print("Wrong username or password")

            if username == "admin" and password == "admin":
                print("Welcome admin!")
                return True
            
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
    words = read_secret_word_database().strip("\n")
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
    edit = "Edit secret word database"
    play = "Play"
    check = "Check highscore"
    quit_game = "End game"
    game_on = True
    print("\nWelcome to hangman game!")


    while game_on:
        print("\n1: ", play)
        print("2: ", check)
        print("3: ", edit)
        print("0: ", quit_game)

        player_input = int(input("\nWhat do you want to do?\n"))
        try:
            if player_input != -1:
                if player_input == 1:
                    while True:
                        player_name = input("What is your name?\n")
                        check_name = ask_name(player_name)
                        if check_name:
                            break
                        else:
                            print("Your name must start with a capital letter and be at least two letters long.")
                    
                    starting_time = int(time.time())
                    file_name = hangman_game()
                    print(f"file_name: {file_name}")
                    if file_name != None:
                        file = f"{file_name}.txt"
                        highscore = int(time.time()) - starting_time
                        save_highscore_files(player_name, highscore, file)
                        print(highscore, "seconds\n")
                
                elif player_input == 2:
                    print("\nRetrieving highscores\n")
                    read_highscore()

                elif player_input == 3:
                    access_ok = log_in()
                    if access_ok:
                        player_input = int(input("\nIf you want to remove a word, give 1. If you want to add new words to database, give 2: \n"))
                        if player_input == 1:
                            remove_form_database()
                            while True:
                                answer =input("Do you want to remove more word? y/n: ")
                                if answer == "y":
                                    remove_form_database()
                                elif answer == "n":
                                    break
                        elif player_input == 2:
                            add_to_database()
                            while True:
                                answer =input("Do you want to add more word? y/n: ")
                                if answer == "y":
                                    add_to_database()
                                elif answer == "n":
                                    break
                
                elif player_input == 0:
                    print("Thanks for playing!")
                    break
        except:
            print("Your chosen option is not on the list.")
main()