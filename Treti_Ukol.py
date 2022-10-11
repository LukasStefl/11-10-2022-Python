num = int(input("Vlož číslo s nělokia číslicemi: "))
count = 0

while num != 0:
    num //= 10
    count += 1

print("Počet číslic:" + str(count))