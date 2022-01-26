def call_my_name():
    print("Minna")
call_my_name()

def return_my_name(name):
    return name
print(return_my_name("Minna"))

def output(word, count):
    print(f"{word * count}")
output("hello", 2)

def get_max(int1, int2, int3):
    largest = 0
    if int1 > largest:
        largest = int1
    if int2 > largest:
        largest = int2
    if int3 > largest:
        largest = int3
    return largest    
largest = get_max(1,4,3)
print(largest)