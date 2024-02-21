import colorama
while True:
    print(colorama.Fore.MAGENTA + "Benvinguts a pycalc, introduiu una de les següents opcions:\n")
    print(colorama.Fore.RED + '0. Sortir \n')
    print(colorama.Fore.GREEN + '1. Sumar \n')
    print(colorama.Fore.WHITE + '2. Restar \n')
    print(colorama.Fore.BLUE + '3. Multiplicar \n')
    print(colorama.Fore.YELLOW + '4. Dividir\n')
    decisio = input("")
    if decisio == "0":
        break
    elif decisio == "1":
        num1 = float(input(colorama.Fore.GREEN + "Digues el primer numero que vols sumar "))
        num2 = float(input(colorama.Fore.GREEN + "Digues el segon numero que vols sumar "))
        resultat = num1 + num2
        print(colorama.Fore.CYAN + "La suma es:", num1, " + ", num2, " = ", resultat)
    elif decisio == "2":
        num1 = float(input(colorama.Fore.WHITE + "Digues el primer numero que vols restar "))
        num2 = float(input(colorama.Fore.WHITE + "Digues el segon numero que vols restar "))
        resultat = num1 - num2
        print(colorama.Fore.CYAN + "La resta es:", num1, " - ", num2, " = ", resultat)
    elif decisio == "3":
        num1 = float(input(colorama.Fore.BLUE + "Digues el primer numero que vols multiplicar "))
        num2 = float(input(colorama.Fore.BLUE + "Digues el segon numero que vols multiplicar "))
        resultat = num1 * num2
        print(colorama.Fore.CYAN + "La suma es:", num1, " * ", num2, " = ", resultat)
    elif decisio == "4":
        num1 = input(colorama.Fore.YELLOW + "Digues el primer numero que vols dividir ")
        num2 = input(colorama.Fore.YELLOW + "Digues el segon numero que vols dividir ")
        if num2 == "0":
            print(colorama.Fore.CYAN + "El resultat es infinit")
        else:
            resultat = float(num1) / float(num2)
            print(colorama.Fore.CYAN + "La suma es:", num1, " / ", num2, " = ", resultat)4
    else:
        print(colorama.Fore.BLACK + "Digues una de les opciones mostrades segons la numeracio ")
print(colorama.Fore.BLACK + "Gracies per utilitzar software de Biel Corporatyon")
