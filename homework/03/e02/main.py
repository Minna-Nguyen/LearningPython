from string_helper import is_name

user_name = input("Your name: ")

if is_name(user_name):
    print(f"Hello {user_name}")
else:
    print("Who are you? Name should be 'first name' and 'last name' format")