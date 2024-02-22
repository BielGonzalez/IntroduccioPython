numero = 1
while numero <= 10:
    contador = 1
    a = 0
    while contador <= numero:
        if numero % contador == 0:
            a+=1
        contador += 1
    if a == 2:
        print(numero)
    numero +=1
