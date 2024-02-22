while True:
    a = 0
    print("Benvingut al software Biel corporatyon")
    print("1.Sumar sol numeros parells")
    print("2.Sumar sol numeros imparells")
    print("3.Sortir")
    decisio = input("")
    num = int(input("Digues un numero. "))
    if decisio == "1":
        while True:
            if num % 2 == 0:
                a += num
            if num == 0:
                print(a)
                break
            num -= 1
    elif decisio == "2":
        while True:
            if num % 2 != 0:
                a += num
            if num == 0:
                print(a)
                break
            num -= 1
    elif decisio == "3":
        break
    else:
        continue
