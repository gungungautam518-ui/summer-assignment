num1 = int (input("enter the starting range:"))
num2 = int (input("enter the ending range:"))
org = 0
for i in range(num1 , num2 + 1):
    temp = i
    while temp > 0:
        digit = temp % 10
        org = org + digit ** digits
        temp = temp // 10
    if org == i:
        print(org, end=" ")
    

