num = int(input("enter a number: "))
pro = 1
temp = num
if temp < 0 :
    print("Error enter a positive  number")
else: 
    while temp > 0 :
        r = temp % 10
        pro *= r
        temp = temp // 10    
    print("the product of digit of ", num , "is" ,pro)