num = int(input("enter no of elemenets:"))
a = []
countodd  = 0
counteven = 0
for  i in range(num):
    a.append(int(input("enter no:")))
for i in range(num):
    if a[i] % 2 == 0:
        counteven +=1
    else:
        countodd +=1
print("total odd no", countodd)        
print("total even no ",counteven)                     