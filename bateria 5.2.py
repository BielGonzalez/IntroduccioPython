llista = []
while True:
    num = input("Digues un numero")
    if "final" in num:
        print("Aquest son els numeros que has dit:", llista)
        break
    else:
        llista.append(int(num))
llista.sort()
print("Ordenada", llista)
llista.sort(reverse=True)
print("Ordenada al reves", llista)
