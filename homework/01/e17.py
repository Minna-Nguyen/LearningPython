import random

salainen_luku = random.randint(0, 10)
kayttajan_syote = -1

while kayttajan_syote != salainen_luku:
    print("Arvaa salainen luku (0 - 10)")
    kayttajan_syote = int( input() )

print("oikein!")



