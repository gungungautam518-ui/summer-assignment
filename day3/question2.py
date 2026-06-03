num1 = int(input("enter starting range:"))
num2 = int(input("enter ending range:"))
if num2 or num1 == 2:
    print ("2 ")
i = num1
while i < num2 :
    for j in range (2,i+1):
        if (i % j == 0):
            break
        else:
            print(i)
            break
    i = i+1    



