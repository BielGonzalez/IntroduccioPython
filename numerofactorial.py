import time

num = int(input("Digues un numero. "))
resultat = 1
while num > 0:
    resultat = resultat * num
    num -= 1
    if num == 1:
        print("Carregant...")
        break
time.sleep(3)
print("El resultat es: ",resultat)
