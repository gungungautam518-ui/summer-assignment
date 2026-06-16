num = int(input("enter no of elemenets:"))
a = []
max = 0
min = max
for  i in range(num):
    a.append(int(input("enter no:")))
for i in range(num):
    if a[i] > max:
        max = a[i]
for i in range(num):
    if a[i] < min:
        min = a[i]      
print(max,min)              