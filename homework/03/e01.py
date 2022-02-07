# printing 1 to 10
for index in range(1,11):
    # last index of range
    if index == 10:
        print(index, end = "")
    else:
        print(index, end = ",")
print()
# printing every second index from 0 to 10
for index in range(0,12, 2):
    # last index of range
    if index == 10:
        print(index, end = "")
    else:
        print(index, end = ",")

print()
# # print 10 to 0
for index in range(10,-1, -1):
    # last index of range
    if index == 0:
        print(index, end = "")
    else:
        print(index, end = ",")
print()