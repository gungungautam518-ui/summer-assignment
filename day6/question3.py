
num = int(input("Enter an integer: "))
count = 0
original_num = num
while num > 0:
    num &= (num - 1)  
    count += 1       

print("The number of set bits in" ,original_num," is:" ,count)
