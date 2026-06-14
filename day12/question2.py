def isamstrong(num):
    temp = num 
    sum = 0
    while temp > 0:
        digit = temp % 10 
        cube = digit * digit * digit
        sum = cube + sum
        temp = temp //10
    if (sum == num):
        print("amstrong no ")
    else :
        print("not an amstrong number")
num = int(input("enter a no :"))
isamstrong(num)


