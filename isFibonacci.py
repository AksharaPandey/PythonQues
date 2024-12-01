def is_fibonacci(n):
    a=0
    b=1
    while b<n:
        c=a+b
        a=b
        b=c
    if b==n or a==n:
        return True
    if b>n:
        return False
n=int(input("Enter the number:"))
if is_fibonacci(n):
        print("The number is fibonacci")
else:
        print("The number is not a fibonacci")