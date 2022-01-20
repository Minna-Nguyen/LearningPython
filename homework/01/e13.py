print("Anna luku")
luku = int(input())

itseisarvo = 0
if luku < 0:
    luku * (-1)
    itseisarvo += luku * (-1)
    print("Antamasi lukusi on")
    print(itseisarvo)
else:
    print("Antamasi luku on")
    print(luku)