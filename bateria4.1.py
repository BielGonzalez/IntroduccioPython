num = int(input("Digues un numero. "))
resultat = num
while resultat > 1:
    if resultat == 0:
        print("0")
    elif num % resultat == 0:
            print(resultat)
            resultat -=1
    elif num % resultat != 0:
            resultat -=1
print(1)
