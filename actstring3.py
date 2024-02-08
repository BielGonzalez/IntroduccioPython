concatenar = ""
while True:
    paraula = input("Digues una paraula: ")
    concatenar = concatenar + " " + paraula
    if "final" in paraula:
        print(concatenar)
        break
    else:
        continue
