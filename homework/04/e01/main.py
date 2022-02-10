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