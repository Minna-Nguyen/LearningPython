def calculate_sum(a, b):
    sum = a + b
    return sum

print(calculate_sum(3,4))


def get_max(int1, int2, int3):
    largest = int1
    if int1 > largest:
        largest = int1
    if int2 > largest:
        largest = int2
    if int3 > largest:
        largest = int3
    return largest    
largest = get_max(1,4,3)
print(largest)