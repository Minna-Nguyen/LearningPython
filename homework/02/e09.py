def reverse(name):
    reversed = ""

    # nimen pitkä pituus laskee nollaan, yksi kerrallaan
    for character in range(len(name) - 1, -1 ,-1):
        reversed += name[character]
    return reversed
print(reverse("Minnulii"))