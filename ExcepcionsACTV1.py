num1 = input("Digues el primer numero a dividir ")
num2 = input("Digues el segon numero a dividir ")
resultat = 0
try:
    resultat = float(num1) / float(num2)
    print(resultat)
except:
    print("Error a la divisio")
