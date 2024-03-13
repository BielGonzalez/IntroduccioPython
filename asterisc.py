moviments = ["|"," ", " ", " ", " ",  " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"]
pos_x = 9
pos_y = 5
ALTURA = 10
AMPLADA = 20
num_linea = 0
cadena_buida = "|" + " " * AMPLADA + "|"
cadena_vora = "-" * (AMPLADA+2)
while True:
    cadena = ""
    dir = input(":")
    if dir == "a" and pos_x > 1:
        pos_x -= 1
    elif dir == "d" and pos_x < 20:
        pos_x += 1
    elif dir == "w" and pos_y > 1:
        pos_y -= 1
    elif dir == "s" and pos_y < 8:
        pos_y += 1
    for i in moviments:
        cadena += i
    for i in range(ALTURA):
        if i == pos_y:
            print(cadena)
        elif i == 0 or i == 9:
            print(cadena_vora)
        else:
            print(cadena_buida)
    for i in range(len(moviments)):
        if i == 0 or i == 21:
            moviments[i] = "|"
        elif i == pos_x:
            moviments[i] = "*"
        else:
            moviments[i] = " "
