# program to get sum of first n natural number , where n is input by user

n = int(input("Enter a natural number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum of the first",n,"natural numbers is:", total)


