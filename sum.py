num=int(input("enter the number you want to add"))
if num<0:
    print('Please enter a +ve number')
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
    print(sum)