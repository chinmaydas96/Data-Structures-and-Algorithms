a = [0, 200, 375, 550, 750, 950]
fuel  =  []

n = len(a)

def minRefill(a,n):
	numRefill = 0
	currentRefill = 0

	while (currentRefill <= n):
		lastRefill = currentRefill
		while (((currentRefill <= n) and (a[currentRefill + 1] -a[lastRefill]<=400))):
			currentRefill += 1
		if currentRefill == lastRefill :
			break
		if currentRefill <= n:
			numRefill +=1
		
	return numRefill		


print minRefill(a,n)			
