import os
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
Module that will create a new text file and save player's highscore of the words. 
"""
def make_player_db(name, secret, highscore):
    """This function will create new text file named after the player's name and list all the highscore of the words.
    Parameter
    ---------
    name: 'String'
        This string is the name of the player. Using the this string name, function will generate a text file.
    Return
    ------
    value: 'String'
        Return a text file.
    """

    # open_file = open(f"{name}.txt", "w")
    open_file = open(f"{name}.txt", "a")
    open_file.write(f'{secret}, {highscore} seconds \n')
    open_file.close()
    return open_file


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
            print("You lost!")
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
    choices =[play, check, quit_game]

    print("Welcome to hangman game!\n")
    i = 0
    for choice in choices:
        i+=1
        print(f'{i}: {choice}')
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
            secret_word = hangman_game()
            highscore = int(time.time()) - starting_time
            make_player_db(player_name, secret_word, highscore)
            print(int(time.time()) - starting_time, "seconds")
        
        elif choices[user_input-1] == check:
            print("Retrieving your highscore \n")
            
            for file in os.listdir("..\src"):
                if file.endswith(".txt") and not file.endswith("words.txt"):
                    print(os.path.join(file))
        
        elif choices[user_input-1] == quit_game:
            print("Thanks for playing!")

main()