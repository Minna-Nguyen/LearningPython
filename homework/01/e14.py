print("Anna kuukausi (1 - 12)")
kuukausi = int(input())
print("Anna päivämäärä (1 - 31)")
päivämäärä = int(input())

if kuukausi == 12 and päivämäärä == 24:
    print("Hyvää joulua!")
elif (kuukausi == 0 or kuukausi > 12) or (päivämäärä == 0 or päivämäärä > 31):
    print("Annoit kummallisen kuukauden tai päivämäärän...")
else:
    print("Vielä ei ole joulu. Harmi!")