import random


def dau_6():
    numero = random.randint(1, 6)
    print(numero)


def daus_6():
    num_daus_usr = int(input("Quants daus vols tirar?"))
    for i in range(1, num_daus_usr + 1):
        tirada = random.randint(1, 6)
        print(tirada)


def dau_x():
    num_cares_usr = int(input("Amb quantes cares vols que siguin?"))
    tirada_daux = random.randint(1, num_cares_usr)
    print(tirada_daux)


def daus_x():
    num_daus_usr = int(input("Quants daus vols tirar?"))
    num_cares_usr = int(input("Amb quantes cares vols que siguin?"))
    for i in range(1, num_daus_usr + 1):
        tirada_daux = random.randint(1, num_cares_usr)
        print(tirada_daux)
