num1 = int(input("enter first no :"))
num2 = int(input("enter second no:"))
greater = 0
smaller = 0
if num1 > num2 :
    greater = num1
    smaller = num2
else :
    greater = num2
    smaller = num1
while greater % smaller != 0 :
    rem = greater % smaller
    greater = smaller 
    smaller = rem
print(rem)    
