import random
# arvotaan satunnaisluku 0 - 10 väliltä
salainen_luku = random.randint(0, 10)
kayttajan_syote = -1

laskuri = 0
while kayttajan_syote != salainen_luku:
    print("Arvaa salainen luku (0 - 10)")
    kayttajan_syote = int( input() )
    laskuri += 1

print("Oikein!", "Arvasit näin monta kertaa:")
print(laskuri)