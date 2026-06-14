def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return  b
    else :
        return c
    
a = int(input("enter a no :"))
b = int(input("enter a no :"))
c = int(input("enter a no :"))
print(max(a,b,c))