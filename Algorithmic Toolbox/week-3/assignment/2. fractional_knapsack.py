# Uses python3

def get_optimal_value(items, capacity, weights, values):

	value = 0
	A = [0] * items

	for i in range(items):
		if capacity == 0:
			return value
		else:
			b = max_index(values, weights, items)
			a = min(weights[b], capacity)
			value = value +  a * (values[b] / weights[b])
			weights[b] -= a
			values[b] -= value
			A[i] = A[i] + a
			capacity -= a
	return value
	

def max_index(values,weights,items):
	index = -1
	maximum = 0
	for i in range(items):
		if ( weights[i] > 0 and maximum < values[i] / weights[i]):
			maximum  = values[i] / weights[i]
			index = i
	return index


if __name__ == "__main__":
    values = []
    weights = []
    n = input().split()
    items = int(n[0])
    capacity = int(n[1])
    for i in range(1, items + 1):
        m = input().split()
        values.append(int(m[0]))
        weights.append(int(m[1]))   
    print ("%.4f" % get_optimal_value(items, capacity, weights, values))
