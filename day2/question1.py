num = int(input("enter a number: "))
sum = 0
temp = num
if temp < 0 :
    print("Error enter a positive  number")
else: 
    while temp > 0 :
        r = temp % 10
        sum = sum  + r
        temp = temp // 10    
    print("the sum of digit of ", num , "is" ,sum)