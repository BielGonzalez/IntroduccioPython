llista = []
while True:
    num = input("Digues un numero")
    llista.append(num)
    if "final" in num:
        llista.pop(-1)
        print(llista)
        break
