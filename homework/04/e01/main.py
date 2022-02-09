from random import randint

# A set is a collection which is unordered, unchangeable, and no duplicates
lotto_numbers = set()

# this will print 7 random number elements that are not duplicate (unique numbers)
while len(lotto_numbers) < 7:
    lotto_numbers.add(randint(1,40))

print(lotto_numbers)