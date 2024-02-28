moviments = [" ", " ", " ", " ",  " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
vides = int(input("Quantes vides tens?"))
while True:
    mov = input("")
    if mov == "a":
        posicion_asterisc = moviments.index("*")
        if posicion_asterisc == 0:
            print(moviments)
            for i in moviments:
                print(type(i))
        else:
            moviments.pop(posicion_asterisc)
            moviments.insert(posicion_asterisc - 1, "*")
            print(moviments)
            for i in moviments:
                print(type(i))
    if mov == "d":
        posicion_asterisc2 = moviments.index("*")
        if posicion_asterisc2 == 19:
            print(moviments)
        else:
            moviments.pop(posicion_asterisc2)
            moviments.insert(posicion_asterisc2 + 1,"*")
            print(str(moviments))
    if mov == "k":
        vides -= 1
    if vides == 0:
        print("Game Over")
        break


