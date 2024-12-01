def display(n1,n2):
    result=[]
    for i in range(1000,2000+1):
        if i%7==0 and i%5!=0:
            result.append(i)
    return result
n1=1000
n2=2000
print(display(n1,n2))