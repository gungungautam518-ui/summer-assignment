def palindrome(num):
    org = num
    rev = 0
    while org > 0:
        digit = org % 10 
        rev = rev * 10 + digit
        org = org //10
    if num == rev:
        print("palindrome no") 
    else :
        print("not a palidrome no")       
num = int(input("enter a no:"))  
palindrome(num)  