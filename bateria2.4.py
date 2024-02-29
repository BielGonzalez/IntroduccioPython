nota = input("Quina es la teva nota? ")
nota = round(float(nota))
if nota == 9 or nota == 10:
    print("La teva nota es un Exel·lent")
elif nota == 7 or nota == 8:
    print("La teva nota es un Notable")
elif nota == 6:
    print("La teva nota es un Bé")
elif nota == 5:
    print("La teva nota es un Suficient")
elif nota <= 4:
    print("La teva nota es un Insuficient ")
