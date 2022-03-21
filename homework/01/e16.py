print("Tulosteetaan luvut väliltä 0 - 9")
i = 0
while i < 10:
    print(i)
    i += 1

print("\n" + "Tulostetaan luvut väliltä 1 - 10")
#tulostetaan luvut 1 - 10
i = 1
while i < 11:
    print(i)
    i += 1

print("\n" + "Tulostetaan luvut 10 - 1")
i = 10
while i > 0:
    print(i)
    i -= 1

print("Anna jokin luku")
luku = int(input())
print()
i = 0
while i <= luku:
    print(i)
    i += 1 