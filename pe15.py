#Project Euler 15
#Lattice paths
#Problem 15
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?
def Gsize(a):
    c1=1
    c2=1
    for i in range(1,a+1):
        c1*=(a+i)
        c2*=i
    return c1/c2
print Gsize(20)
exit()

#output
#137846528820
