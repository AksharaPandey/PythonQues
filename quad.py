import cmath
a=1
b=6
c=3
#d=b2-4ac
d=(b**2)-4*a*c
#formula=-b+-root{d}/2a
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print("the solutions are {0} and {1}".format(sol1,sol2))