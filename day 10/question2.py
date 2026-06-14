num = int(input("enter a number of rows:"))
for i in range(1,num+1):
    j = 0
    while (j < i):
        print(" ",end = " ")
        j +=1
    k = 5
    while(k >=i):
        print("*",end =" ")  
        k -= 1    
    l = num
    while (l >i):
        print("*",end =" ")
        l-=1
    print()    