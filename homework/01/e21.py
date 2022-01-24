print("Anna suorakaiteen korkeus")
korkeus = int(input())
print("Anna suorakaiteen leveys")
leveys = int(input())
MääräKorkeus = 0 # rivi
MääräLeveys = 0 # sarake

while MääräKorkeus < korkeus:
  while MääräLeveys < leveys:
    # Tulosta "X" ilman enter painallusta.
    print("X", end = '')
    MääräLeveys += 1
  # Nollataan MääräLeveys jotta päästän takaisin loopin sisään (rivi 9).
  MääräLeveys = 0
  # Tulosta enter
  print()
  MääräKorkeus += 1