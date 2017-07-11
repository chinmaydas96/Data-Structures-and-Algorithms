# Uses python3

def binary_search(a, x):
	low, high = 0, len(a)
	while(low < high):
		mid = low + (high - low)//2
		
		if (x == a[mid]):
			return mid 
		elif (x < a[mid]):
			high = mid - 1
		else:
			low = mid + 1	

	if (low == len(a) or a[low] != x):
		return -1
	else:
		return low		    		 	

def search(b,a):
	data = [] 
	for i in b:
		data.append(binary_search(a,i))
	return data

if __name__ == '__main__':

	x = input().split()
	y = input().split()	
	a = [int(num) for  num in x[1:]]
	b = [int(num) for  num in y[1:]]
	out = search(b,a)
	for i in out:
		print(i,end=" ")
