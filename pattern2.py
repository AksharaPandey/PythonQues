rows=int(input("Enter the row number:"))
for i in range(1,rows+1):
    for j in range(1,1+i):
        print("*", end=" ")
    print()
for i in range(rows ,1,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()