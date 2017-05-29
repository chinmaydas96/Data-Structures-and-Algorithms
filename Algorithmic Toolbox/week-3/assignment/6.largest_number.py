# Uses python3


def largest_number(a):
    # write your code here
    res = ""
    sort = []
    
    for i in range(len(a)):
    	max_index = sorted_element(a)
    	sort.append(a[max_index])
    	del a[max_index]
    
    for x in sort:
        res += str(x)
    return res

def sorted_element(array):
	max = array[0]
	index = 0
	
	for i in range(len(array)):
		if (array[i] >= max):
			max = array[i]
			index = i
	return index				

if __name__ == '__main__':
    n = int(input())
    data = [int(x) for x in input().split()]
    print(largest_number(data))
