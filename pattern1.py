n=int(input("Enter the value:"))
for i in range(1,n+1):
    for j in range(i,2*i):
        print(j%2, end= " ")
    print()