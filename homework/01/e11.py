print("luku 1")
luku1 = int( input() )
print("luku 2")
luku2 = int( input() )
print("minkä laskutoimituksen haluat tehdä? +, -, /, *")
operaattori = input()

if operaattori == "+":
    print(luku1 + luku2)
elif operaattori == "-":
    print(luku1 - luku2)
elif operaattori == "/":
    #jos luku2 ei ole 0, suorita jakolasku, muulloin tulee virheilmoitus
    if luku2 != 0:
        print(luku1 / luku2)
    else:
        print("Virhe! Nollalla ei saa jakaa")
elif operaattori == "*":
    print(luku1 * luku2)
else:
    print("Anna +, -, /, * syötteeksi")
