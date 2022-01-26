boolean = True # true = 1, false = 0
int_number = 28
int_number2 = 13
float_number = 5.5
# classes correctly
print(boolean, type(boolean))
print(int_number, type(int_number))
print(float_number, type(float_number), "\n")
#converting object to string
print(boolean, type(str(boolean)))
print(int_number, type(str(int_number)))
print(float_number, type(str(float_number)), "\n")

print(f"Testing boolean + boolean: {boolean + boolean}")
print(f"Testing int + int: {int_number + int_number}")
print(f"Testing string + string: {str(int_number) + str(int_number)}", "\n")

print(f"Float to int: {int(float_number)}")
print(f"Float to int (rounded): {round(float_number)}")
print(f"Int to float: {float(int_number)}")
print(f"Summing two int: {int_number + int_number2}. The type is: {type(int_number + int_number2)}")
print(f"Summing int and float: {int_number + float_number}. The type is: {type(int_number + float_number)}")
print(f"Division of two int: {int_number / int_number2}. The type is: {type(int_number / int_number2)}")