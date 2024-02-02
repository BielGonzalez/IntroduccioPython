num = int(input("Digues un numero. "))
num1 = num
a = 1
valor_original = num
while True:
    num = num + a
    a += 1

    if a == num1:
        print(num)
        break
