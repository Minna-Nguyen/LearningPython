print("Anna kuukausi (1 - 12)")
kuukausi = int(input())
print("Anna päivämäärä (1 - 31)")
päivämäärä = int(input())

if (kuukausi == 12 and päivämäärä == 6) or (kuukausi == 5 and päivämäärä == 1): 
    print("Nyt on itsenäisyyspäivä tai vappu")
elif (kuukausi == 0 or kuukausi > 12) or (päivämäärä == 0 or päivämäärä > 31):
    print("Annoit kummallisen kuukauden tai päivämäärän...")
else:
    print("Nyt ei ole itsenäisyyspäivä tai vappu")