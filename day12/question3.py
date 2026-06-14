def fibonacci(num):
    firsterm = 0
    nextterm = 1
    for i in range(1,num+1):
        print(firsterm , end = " ")
       
        temp = firsterm + nextterm
        firsterm = nextterm
        nextterm = temp
       
num = int(input("enter no of terms:"))
fibonacci(num)        