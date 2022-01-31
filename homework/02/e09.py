def reverse(name):
    reversed = ""
    # range(0,9) -> 0 - 8
    x = range(len(name)+1)
    
    for x in name:
        reversed = x + reversed
    return reversed
print(reverse("Minnulii"))