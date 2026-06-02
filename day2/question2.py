# program to print reverse of a number

num = int(input ("enter a number :"))
rev = 0 
temp = num
while temp > 0:
    digit = temp % 10
    rev = (rev * 10 ) + digit
    temp= temp //10
print("the reverse of ",num, "is",rev)       

