#project Euler 32

import itertools
from time import time

n=9
num = sum([i*10**(n-i) for i in range(1,n+1)])
print num
panDigitalList = set([s for s in str(num)])
print panDigitalList

def euler34(panDigitalList):
	totalSumSet = set([])
	for i in range(1,4):
		for j in range(1,6-i):

			perm1 = itertools.permutations(panDigitalList,i)
			for p in perm1:
				perm2Set = panDigitalList - set(p)
				perm2 = itertools.permutations(perm2Set,j)
				for q in perm2:
					leftSet = panDigitalList-set(p)-set(q)
					n1,n2 = int("".join(p)), int("".join(q))
					n3 = n1 * n2
					n123str = "".join(p) + "".join(q) + str(n3)
					if panDigitalList==set(tuple(str(n3))+p+q) and len(n123str)==len(panDigitalList):
						print n1,'*',n2,'=',n3
						totalSumSet.add(n3)
	totalSum = 0
	for s in totalSumSet:
		totalSum+= s
	return totalSum

start = time()
tot = euler34(panDigitalList)
end = time()

print "Total is",tot,"found in",end-start,"seconds"
