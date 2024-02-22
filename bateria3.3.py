num = int(input("Digues un numero"))
a = 0
while True:
    if num % 2 == 0:
        a += num
    if num == 0:
        break
    num-=1
print(a)
