from random import randint

user_lotto = {1, 2, 3, 4, 5, 6, 7}

weeks = 0
correct_count = 1

def generate_lotto_numbers(a,b):
# A set is a collection which is unordered, unchangeable, and no duplicates
    lotto_numbers = set()
    if type(a) != int or type(b) != int:
        raise Exception("Must be an int type!")
    else:
    # this will print 7 random number elements that are not duplicate (unique numbers)
        while len(lotto_numbers) < 7:
            lotto_numbers.add(randint(a,b))
    return lotto_numbers

"""1 week = one while loop iteration, 52 weeks = 1 years"""
def weeks_and_years(count):
    if count == 1:
        print(f"It took {count} week.")
    elif count > 1 and count <= 51:
        print(f"It took {count} weeks.")
    elif count == 52:
        print(f"It took {count} year.")
    else:
        print(f"It took {count * 0.019230:.0f} years")


while True:
    random_lotto = generate_lotto_numbers(1,40)
    # same_values is a set()
    # checking the intersection of user_lotto and random_lotto
    same_values = user_lotto.intersection(random_lotto)
    weeks += 1
    # kattoo onko 7 kpl oikeata numeroa alottaen 1
    if correct_count == len(same_values):
        print(f"You got {correct_count} correct! New higscore!")
        correct_count += 1
        weeks_and_years(weeks)
        print()

    if correct_count == 8:
        break

"""04/E03 excersise starts"""

# def generate_lotto_numbers_one(int_a,int_b,int_c):
#     # A set is a collection which is unordered, unchangeable, and no duplicates
#     lotto_numbers = set()
#     if type(int_a) != int or type(int_b) != int:
#         raise Exception("Must be an int type!")
#     else:
#     # this will print 7 random number elements that are not duplicate (unique numbers)
#         while len(lotto_numbers) < int_c:
#             lotto_numbers.add(randint(int_a,int_b))
#         return lotto_numbers
# # outputs seven random unique numbers between 1 - 40
# print(generate_lotto_numbers_one(1, 40, 7))

# def generate_lotto_numbers_two(min,max,amount):
#     lotto_numbers_two = set()

#     if type(min) != int or type(max) != int:
#         raise Exception("Must be an int type")
#     else:
#         while len(lotto_numbers_two) < amount:
#             lotto_numbers_two.add(randint(min,max))
#         return lotto_numbers_two
# # outputs seven random unique numbers between 1 - 40
# print(generate_lotto_numbers_two(min=1,max=40,amount=7))

# def generate_lotto_number_three():
#     lotto_numbers_three = set()

#     while len(lotto_numbers_three) < 7:
#         lotto_numbers_three.add(randint(1,40))
#     return lotto_numbers_three

# # outputs seven random unique numbers between 1 - 40
# print(generate_lotto_number_three())

# def generate_lotto_numbers_four(min,max,amount):
#     lotto_numbers_four = set()

#     while len(lotto_numbers_four) < amount:
#         lotto_numbers_four.add(randint(min,max))
#     return lotto_numbers_four

# # # outputs four(4) random unique numbers between 1 - 10
# print(generate_lotto_numbers_four(min=1,max=10,amount=4))

# def generate_lotto_numbers_five(min, max, amount):
#     lotto_numbers_five = set()

#     while len(lotto_numbers_five) < amount:
#         lotto_numbers_five.add(randint(min,max))
#     return lotto_numbers_five
# # outputs six (6) random unique numbers between 1 - 6 
# # (which basically is 1, 2, 3, 4, 5, 6)
# print(generate_lotto_numbers_five(min=1,max=6,amount=6))

# def generate_lotto_numbers_six(min, max, amount):
#     lotto_numbers_six = set()

#     while len(lotto_numbers_six) < amount:
#         lotto_numbers_six.add(randint(min,max))
#     return lotto_numbers_six
# # crashes the app, you cannot choose seven (7) unique numbers between 1 - 6
# # the amount is 7 in this while loop, but there are only 6 numbers to choose from
# print(generate_lotto_numbers_six(min=1, max=6, amount=7))