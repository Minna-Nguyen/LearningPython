from random import randint

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

print(generate_lotto_numbers(1,40))