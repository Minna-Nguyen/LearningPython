print("What grade did you get? (0 - 5)")
grade = int(input())
in_range = range(0,5)

# checking if user input is valid
while grade < 0 or grade > 5:
    print("What grade did you get? (0 - 5)")
    grade = int(input())

# outputs the result for user's input
if grade == 0:
    print("Fail")
elif grade == 1 or grade == 2:
    print("Weak")
elif grade == 3 or grade == 4:
    print("Good")
elif grade == 5:
    print("Excellent")
