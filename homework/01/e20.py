luku = 0 #käyttäjän syöte myöhemmin
ekaluku = 0 #ensimmäinen talletus
pienin = 0 #talletus pienimmälle luvulle

print("Anna positiivinen luku")
ekaluku = int(input())
if ekaluku < 0:
    print("Et antanut lukuja.")
else:
    while luku >= 0:
        print("Anna positiivinen numero (lopetus negatiivisella luvulla)")
        luku = int(input())
        if (luku < ekaluku and luku > 0) or luku == 0:
            pienin = luku

    if pienin != -1:
        print("Pienin antamasi luku oli")
        print(pienin)
    else:
        print("Et antanut lukuja.") 