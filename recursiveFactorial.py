def rec_factorial(n):
    if n==1: 
        return n
    else:
        return n*rec_factorial(n-1)
num=int(input("Enter the number:"))
if num<0:
    print("The factorial does not exist for -ve number")
elif num==0:
    print("The factorial of 0 is always 1")
else:
    print(rec_factorial(num))