llista = []
while True:
    num = input("Digues un numero")
    llista.append(num)
    if "final" in num:
        llista.pop(-1)
        break
resultat = 0
for i in llista:
    resultat = resultat + int(i)
print(resultat)
