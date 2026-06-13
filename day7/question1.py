num = int(input("enter a no:"))
original_num = num

stack = []


while num > 1:
    stack.append(num)
    num -= 1
result = 1

while stack:
    result *= stack.pop()

print("The factorial of ",original_num,"is ",result)
