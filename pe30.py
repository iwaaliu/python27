#project Euler 30
def digSum(bot, top, digFunctionList):
	tot = 0
	for i in range(bot,top):
		if i==sum([digFunctionList[int(d)] for d in str(i)]):
			print '\t',i
			tot+=i
	return tot

def fact(n):
	if n<=1:
		return 1
	else:
		return fact(n-1)*n

factList = [fact(i) for i in range(10)]

digFifths = [i**5 for i in range(10)]

print 'prob 1:', digSum(3, 1000000, digFifths)

print '-'*80

print 'prob2 2:' digSum(3, 1000000, factList)
