# program to check strong no . 

num = int(input("enter a value to check strong no :"))

sum = 0
temp = num

while temp > 0 :
    fact = 1 
    digit = temp % 10
    for i in range(1,digit+1):
        fact = fact * i
    temp = temp // 10 
    sum = sum + fact
if (num == sum):
    print("it is a strong no ")
else :
    print("it is not a strong no")            