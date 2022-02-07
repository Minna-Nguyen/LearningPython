from string_helper import is_name
ask_ignore_case = input("Ignore case? 'y/n' \n")

while True:
    if ask_ignore_case == "y":
        answer = True
        break
    elif ask_ignore_case == "n":
        answer = False
        break
    else:
        print("Ignore case? Please type 'y' or 'n'")
        valid_answer = input()
        
        if valid_answer == "y":
            answer = True
            break
        elif valid_answer == "n":
            answer = False
            break
user_name = input("Your name: ")

if is_name(user_name, answer):
    print(f"\nHello {user_name}")
else:
    print("Who are you? Name should be 'first name' and 'last name' format")