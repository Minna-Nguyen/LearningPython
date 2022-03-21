#!/bin/python3

print("Anna neliön korkeus")
korkeus = int( input() )
rivi = 0
while rivi < korkeus:

  sarake = 0
  while sarake != korkeus:
    # Tulosta "X" ilman enter painallusta
    # Huom! tämä vaatii python3 - tulkin joka asetettu päälle rivillä 1
    print("X", end='')
    sarake = sarake + 1

  # Tulosta enter
  print()
  rivi = rivi + 1 