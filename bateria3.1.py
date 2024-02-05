num = int(input("Digues un numero. "))
num1 = num
a = 1
while True:
    num = num1 * a
    print(num)
    a += 1
    num = num1
    if a == 11:
        break
