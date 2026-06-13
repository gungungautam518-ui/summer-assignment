
terms = int(input("enter a no:"))  

fib_sequence = [0, 1]  

while len(fib_sequence) < terms:
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
print(f"Fibonacci sequence up to {terms} terms:")
print(fib_sequence[:terms])
