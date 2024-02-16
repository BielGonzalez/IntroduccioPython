llista = []
llista_parells = []
llista_imparells = []
while True:
    num = input("Digues un numero")
    if "final" in num:
        break
    else:
        num = int(num)
    if num % 2 == 0:
        llista_parells.append(num)
    else:
        llista_imparells.append(num)
print("Aquesta es la llista de imparells", llista_imparells)
print("Aquesta es la llista d'imparells", llista_parells)
