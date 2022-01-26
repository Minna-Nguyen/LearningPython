print("hello world")
a = "hello"
b = "world"

# this one will only print "hello"
print(a)
# prints "hello world", there is a space between 'a' and 'b'
print(a, b)

# prints "hello" and 
# "world" on two different lines
print(a)
print(b)

"""
This is a multiline comment
prints "hello;world"

"""
print(a, b, sep =":")
# prints "hello:world;"
print(a, b, sep =":", end = ";")
print("\n")

str1 = "what"
str2 = "is this"
#"\n" makes an extra enter
print(str1, "\n")
print(str2)
# prints "helloworld"
print(a, end = '')
print(b)
