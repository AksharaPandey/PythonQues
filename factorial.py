num=int(input("Enter the factorial:"))
factorial=1
if (num<0):
    print("The factorial for the -ve number do not exist")
elif (num==0):
    print("The factorial for 0 is always 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
        print(factorial)