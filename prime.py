num=int(input("Enter the number"))
if num==1:
    print("Number is not a prime")
elif num>1:
    for i in range(2,num):
        if(num%i)==0:
            print("Number is not a prime")
        else:
            print("It is a prime number")
else:
    print("Prime number")