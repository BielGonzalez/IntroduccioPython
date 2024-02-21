import random

tirada_dau = random.randint(1, 6)
print(tirada_dau)


def dau_6():
    numero = random.randint(1,6)
    print(numero)

dau_6()

def daus_6():
    num_daus_usr = int(input("Quants daus vols tirar?"))
    for i in range(1,num_daus_usr+1):
        tirada = random.randint(1,6)
        print(tirada)
daus_6()

def dau_x():
    num_cares_usr = int(input("Amb quantes cares vols que siguin?"))
    tirada_daux = random.randint(1, num_cares_usr)
    print(tirada_daux)
dau_x()
def daus_x():
    num_daus_usr = int(input("Quants daus vols tirar?"))
    num_cares_usr = int(input("Amb quantes cares vols que siguin?"))
    for i in range(1,num_daus_usr+1):
        tirada_daux = random.randint(1,num_cares_usr)
        print(tirada_daux)

daus_x()
