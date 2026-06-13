# decimal to binary
num = int(input("enter a decimal num  :"))
if num == 0:
    binary = "0"
else:
    binary = ""
    temp = num
    
    while temp > 0:
        rem = temp % 2          
        binary = str(rem) + binary
        temp = temp // 2         

print("The binary representation of ",num , "is:" ,binary)
