def deTOhex(nbr):
    ent, dec = nbr.split(".")
    bin1 = bin(int(ent))[2::]
    print(bin1)
    if bin1 == "0":
        long = 10
        test = False
    else:
        long = 10 - len(bin1)
        test = True
    temp = float("0." + dec)
    bin2 = ""
    for i in range(long):
        print(temp)
        temp = temp * 2
        if test:
            if temp > 1:
                bin2 += "1"
                temp -= 1
                print("+1")
            else:
                bin2 += "0"
                print("+0")
    print(bin2)


def main():
    menu = """
    Menu :
    
    1 = Décimal vers Héxadécimal
    2 = Héxadéciaml vers Décimal
    Q = Quitter le programme
"""
    print("Bienvenue dans ce programme de conversion de nombre décimal en héxadécimal (et inversement)", menu)
    # key = input("Que voulez-vous faire? ").upper()
    key = "1"
    while key != "Q":
        if key == "1":
            value = input("Nombre décimal? ")
            deTOhex(value)
        if key == "2":
            a = 0


if __name__ == "__main__":
    main()
