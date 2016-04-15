
#brute force is simple, and complexity is O(n)
s=0
n=1000
for i in range(1,1000):
   if(i%3==0 or i%5==0) :
       s+=i
print s

# O(1) method
# sum(3*)+sum(5*)-overlap(3*,5*)
#=sum(3*)+sum(5*)-sum([3*5]*)
# sum(3*) = [3+n-mod(n,3)]/2*n/3

n=n-1 # below n (1000), so we minus 1 as last possible access element.
s3=(3+n-n%3)*(n/3)/2
s5=(5+n-n%5)*(n/5)/2
so=(15+n-n%15)*(n/3/5)/2 #put /2 at the end, or the intermidiate result might be odd, odd/2 will give wrong result
s=s3+s5-so
print s

#output:
#233168
#233168

#if n is big, e.g., n=100000000, time used in 
# method 1 2333333316666668 26.0493518802 (for n=1000, time used is 0.000236084285511)
# method 2 2333333316666668 1.36860455378e-05 (for n=1000, time used is 3.42151138422e-06, almost no change from n=1000)
# 
