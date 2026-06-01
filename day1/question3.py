n = int(input("enter a no to get its factorial : "))
fact = 1
if n < 0:
    print("Error : factorial does not exist for negative no.")
elif n==0:
    print("the factorial of 0 is 1")   
else :
    for i in range(1,n+1):
        fact = fact * i

print("the factorial of",n,"is",fact )




    