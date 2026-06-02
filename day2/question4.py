# program to check palindrome of a number

num = int(input ("enter a number :"))
rev = 0 
temp = num
while temp > 0:
    digit = temp % 10
    rev = (rev * 10 ) + digit
    temp= temp //10

if rev == num:
    print("the enterd no is palindrome")
else:
    print("the enterd no is not palindrome")    


    

       
