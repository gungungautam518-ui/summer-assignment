num = int(input("enter a number of rows:"))
for i in range(1,num+1):
    j = num
    while (j > i):
        print(" ",end = " ")
        j -=1
    k = 1
    while(k <=i):
        print("*",end =" ")  
        k += 1    
    l = 1
    while (l <i):
        print("*",end =" ")
        l+=1
    print()    