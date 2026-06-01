# program to count the total digit of a no.

n = int(input("Enter a number: "))
count = 0
if count == 0:
    print("The number is 0 and it has 1 digit.")
else : 
    while n > 0 :
        count = count + 1
        n = n // 10
        
print("Total digits in the number is:", count)      

   