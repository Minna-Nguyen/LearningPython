print("Anna luku:")
luku = int(input())

if luku < 0:
    while luku < 0:
        print("Anna positiivinen luku")
        positiivinen = int(input())
        #jos käyttäjän antama luku on positiivinen, tulostetaan joka toinen luku ja lähdetään pois silmukasta
        if positiivinen > 0:
            print("Tulostetaan joka toinen luku")
            i = 0
            while i <= positiivinen:
                print(i)
                i += 2
            break
else:
    print("Tulostetaan joka toinen luku")
    i = 0
    while i <= luku:
        print(i)
        i += 2