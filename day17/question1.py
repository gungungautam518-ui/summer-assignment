num = int(input("enter no of elemenets:"))
a = []
for  i in range(num):
    a.append(int(input("enter no:")))
num2 = int(input("enter no of elemenets:"))
b = []
for  i in range(num2):
    b.append(int(input("enter no:")))    
c = a+b
for i in range(len(c)):
    print(c[i],end = " ")     
