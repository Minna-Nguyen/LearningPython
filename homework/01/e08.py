print("Anna ensimmäinen luku")
luku1 = int(input())
print("Anna toinen luku")
luku2 = int(input())

if luku2 != 0:
    jakolasku = luku1 / luku2
    print("Jakolaskun tulos: ")
    print(jakolasku)
else:
    print("Virhe! Nollalla ei saa jakaa")