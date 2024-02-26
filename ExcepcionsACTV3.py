num1 = input("Digues un numero per poder sumar-lo")
num2 = input("Digues un altre numero.")
try:
    resultat = float(num1) + float(num2)
    print(resultat)
except:
    print("Error")
