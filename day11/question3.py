import math
def isprime(num):
    flag =1
    for i in range(1,(num+1)//2):
        if num % i == 0:
            flag = 0
        else :
            flag = 1    

    if flag == 1:
        print("prime no")
    else :
        print("not a prime number")


num = int(input("enter a no:"))    
isprime(num)