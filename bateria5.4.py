def eliminar_palabra():
    while True:
        llista.remove(palabra_buscar)
        if palabra_buscar not in llista:
            break
llista = []
while True:
    paraula_user = input('Diguem una paraula')
    llista.append(paraula_user)
    pregunta = input('Vols saber quantes vegades estava alguna paraula?')
    if pregunta == 'Si' or pregunta == "si":
        palabra_buscar = input('Que palabra desea contar?')
        print("Esta palabra: ", palabra_buscar, "estava este numero de veces en la lista:")
        print(llista.count(palabra_buscar))
        print("Ahora esta palabra sera eliminada de la lista")
        eliminar_palabra()
        print("Ahora esta es la lista actual ", llista)
        salir = input('Desea salir?')
        if salir == 'si' or salir == "Si":
            break
