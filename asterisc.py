moviments = [" ", " ", " ", " ",  " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
vides = int(input("Quantes vides tens?"))
while True:
    mov = input("")
    if mov == "a":
        posicion_asterisc = moviments.index("*")
        if posicion_asterisc == 0:
            # funcion map convierte cada elemento de la lista con la funcion indicada en este caso str.
            lista_convertida = map(str, moviments)
            # Join une todos los strings creados por map anteriormente en uno solo
            resultado = " ".join(lista_convertida)
            print(resultado)
        else:
            moviments.pop(posicion_asterisc)
            moviments.insert(posicion_asterisc - 1, "*")
            # funcion map convierte cada elemento de la lista con la funcion indicada en este caso str.
            lista_convertida = map(str, moviments)
            # Join une todos los strings creados por map anteriormente en uno solo
            resultado = " ".join(lista_convertida)
            print(resultado)
    if mov == "d":
        posicion_asterisc2 = moviments.index("*")
        if posicion_asterisc2 == 19:
            # funcion map convierte cada elemento de la lista con la funcion indicada en este caso str.
            lista_convertida = map(str, moviments)
            # Join une todos los strings creados por map anteriormente en uno solo
            resultado = " ".join(lista_convertida)
            print(resultado)
        else:
            moviments.pop(posicion_asterisc2)
            moviments.insert(posicion_asterisc2 + 1,"*")
            # funcion map convierte cada elemento de la lista con la funcion indicada en este caso str.
            lista_convertida = map(str, moviments)
            # Join une todos los strings creados por map anteriormente en uno solo
            resultado = " ".join(lista_convertida)
            print(resultado)
    if mov == "k":
        vides -= 1
    if vides == 0:
        print("Game Over")
        break
# info de map, join y srt sacada de https://www.freecodecamp.org/news/python-list-to-string-how-to-convert-lists-in-python/
