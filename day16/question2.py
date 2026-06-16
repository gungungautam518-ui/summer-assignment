num = int(input("enter no of elemenets:"))
a = []
sum = 0
avg = 0
for  i in range(num):
    a.append(int(input("enter no:")))
for i in range(num):
    sum = sum + a[i]    
    avg = sum/num 
print("the sum of array element is ",sum)    
print("the avg of array element is ",avg)   