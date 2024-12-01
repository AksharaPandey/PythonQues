year=int(input("Enter the year:"))
if(year%400==0) and (year%100==0):
    print(year," is the leap year")
elif(year%4==0) and (year%100==0):
    print(year," is the leap year")
else:
    print(" is not a leap year")