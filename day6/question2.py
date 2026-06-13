num = input("enter binary no :")
decimal = 0
power = 0
for i in range(len(num) - 1, -1, -1):
    digit = int(num[i])
    decimal += digit * (2 ** power)
    power += 1

print("Decimal value:", decimal)
