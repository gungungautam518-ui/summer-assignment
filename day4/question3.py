
num = int (input("enter a no to check if it is amstrong no."))
temp = num
org = 0
while temp> 0:
    digit = temp % 10 
    cube = digit* digit * digit 
    org = org + cube 
    temp = temp // 10
if num == org:
    print("it is an amstrong no. ")
else:
    print("it is not an amstrong no.")     


