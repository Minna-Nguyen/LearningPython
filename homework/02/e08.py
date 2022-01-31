# function that returns an int between range a - b
def get_int(sentence, a, b):
    grade = int(input(sentence))
    while grade < a or grade > b:
        print("Grade must be 4 - 10")
        grade = int(input())
    return grade
# calling the function
grade = get_int("Give grade:", 4, 10,)
print("You gave:", grade)
    


