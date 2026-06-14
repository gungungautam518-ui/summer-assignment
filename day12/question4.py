n = int(input("enter the no to check perfect no ."))
def check_perfect(n):
    sum = 0
    for i in range(1, n):
        if (n % i == 0):
            sum = sum + i   

    if (sum == n ):
        print("the no is perfect ")
    else :
        print("the no is not perfect")     
check_perfect(n)                                                                                        
