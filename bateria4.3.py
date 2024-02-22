num = int(input("Digues un numero. "))
a = 0
b = 0
while a < num:
    if num % 2 != 0:
        b += num
    if num == 0:
        break
    num -= 1
print(b)
