moviments = ["|"," ", " ", " ", " ",  " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"]
pos_x = 9
pos_y = 0
AMPLADA = 20
num_linea = 0
cadena_buida = "|" + " " * AMPLADA + "|"
cadena_vora = "-" * (AMPLADA+2)
while True:
    cadena = ""
    for i in moviments:
        cadena += i
    print(cadena)
    dir = input(":")
    if dir == "a" and pos_x > 1:
        pos_x -= 1
    elif dir == "d" and pos_x < 20:
        pos_x += 1
    #actualitzem
    for i in range(len(moviments)):
        if i == 0 or i == 21:
            moviments[i] = "|"
        elif i == pos_x:
            moviments[i] = "*"
        else:
            moviments[i] = " "
