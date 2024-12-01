def pyramid(n):
    for i in range(1,n+1):
        for j in range(n-1):
            print(" ",end=" ")
        for k in range(i,2*i):
            print("*",end=" ")
        print()
pyramid(5)