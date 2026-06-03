num = int(input("enter no to cheack if it is prime or not:"))
isprime = True
i= 2
while i < num/2 :
     if (num % i == 0):
          isprime = False 
          break
     i = i + 1    
if isprime :
     print (" prime no ")
else :
     print(" not a prime no ")                   
           
