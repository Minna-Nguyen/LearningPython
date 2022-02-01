# function that returns an int between range a - b

def get_int(sentence, a, b):
    age = int(input(sentence))
    while age < a or age > b:
        print("Age must be between 0 - 120")
        age = int(input())
    return age
# calling the function
age = get_int("Give age: ", 0, 120,)
print("You gave:", age)
    