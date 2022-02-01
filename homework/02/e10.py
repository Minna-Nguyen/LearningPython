def reverse(name, lowercase):
    reversed = ""
    # range(0,9) -> 0 - 8
    if lowercase == True:
        name = name.lower()
        for character in range(len(name) - 1, -1 ,-1):
            reversed += name[character]
        return reversed
    else:
        for character in range(len(name) - 1, -1 ,-1):
            reversed += name[character]
        return reversed
print(reverse("Minnulii", True)) # iilunnim
print(reverse("Minnulii", False)) # iilunniM

