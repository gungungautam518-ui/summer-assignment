num = int(input("enter a no:"))
reversed_num = 0

reversed_num = (reversed_num * 10) + (num % 10)
num //= 10
reversed_num = (reversed_num * 10) + (num % 10)
num //= 10
reversed_num = (reversed_num * 10) + (num % 10)
num //= 10
print("Reversed Number:", reversed_num)
