
num =int(input("enter a no:"))
original_num = num
stack = []
while num > 0:
    last_digit = num % 10
    stack.append(last_digit)
    num //= 10
digit_sum = 0
while stack:
    digit_sum += stack.pop()
print(f"The recursive sum of digits for {original_num} is: {digit_sum}")
