
a = "hello"
b = 'helloo!'
c = """hello
          world"""
d = '''hello
          world'''

print(a)
print(b, "\n")
print(c)
print(d)

# a = "hel'lo" -> hel'lo
# b = 'he"llo' -> he"llo
# c = "hel"lo" -> doesn't print anything!

name = "Athena"
# print("Hello", name)

bmi = 25.113212
# formatted string literal writing way
print(f"Hello {name}, you have bmi = {bmi}")
# modifying the float to display 25.11 instead of 25.113212
print(f"Hello {name}, you have bmi = {bmi:.2f}")
# this is the usual way
print("Hello", name, "you have bmi = ", bmi, "\n")

print("The length of this name is", len(name))
print(f"First letter: {name[0]} and last letter: {name[5]}", "\n")

# testing 7 basic functions related to string
str = "this is a test"
str2 = "what"
print("This string is the original one:", str)

# number 1, islower() -function
# this function will return 'True' if the string starts with a lower case
print(str.islower())

# number 2, capitalize()
#this will convert the first letter to upper case
print(str.capitalize())

# number 3, upper()
# converts a string to upper case 
print(str.upper())

# number 4, center()
# returns a centered string
print(str2.center(10, "-"))

# number 5, partition()
# Returns a tuple where the string is parted into three parts
print(str.partition("is"))

# number 6, rjust()
# Returns a right justified version of the string
print(str2.rjust(10))

# number 7, replace()
# Returns a string where a specified value is replaced with a specified value
print(str.replace("i", "AA"), "\n")

some = input("Say something: ")
some2 = input("Say something: ")
# comparing if the memory address is the same
print(f"Value in memory address {id(some)}")
print(f"Value in memory address {id(some2)}")
# comparing if the content is the same
if some == some2:
    print("The same content: True")
else:
    print("The same content: False")

print(f"Has the same memory address: {id(some) is id(some2)} ")