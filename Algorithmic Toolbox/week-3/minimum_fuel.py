a = [0, 200, 375, 550, 750, 950]
fuel  =  []
i = 0
while(i < 6):
	for j in range(0,len(a)):
		if (a[j] - a[i]) > 400:
			fuel.append(a[j-1])
			break
	i +=1		
print fuel
