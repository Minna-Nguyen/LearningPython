def reverse(name, lowercase):
    reversed = ""
    # range(0,9) -> 0 - 8
    x = range(len(name)+1)
    for x in name:
        x = x.lower()
        reversed = x + reversed
    return f"{reversed} {lowercase}"
    
print(reverse("Minnulii", lowercase=True))
