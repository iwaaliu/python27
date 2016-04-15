#project Euler 
#Problem 16 
#Power digit sum

y=2**1000
r=0
while (y>0):
    r+=y%10
    y=y/10
print r,y

# output
# 1366 0
