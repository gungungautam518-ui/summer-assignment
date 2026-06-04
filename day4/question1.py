n = int (input("enter the no of terms :"))
firsterm = 0 
nexterm = 1
i = 0

while i < n :
    temp = firsterm + nexterm
    firsterm = nexterm
    nexterm = temp
    i = i + 1 
    print(firsterm , end = "  ")    

    