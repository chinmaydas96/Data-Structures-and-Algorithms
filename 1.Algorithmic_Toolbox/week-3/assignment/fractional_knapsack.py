# Uses python3
import sys

def get_optimal_value(capacity=50, values=[60,100,120], weights=[20,50,30]):

    value = 0.
    ratio_dict = {}
    for i in range(len(weights)):
    	ratio_dict[values[i] / weights[i]] =  i

    for i in sorted (ratio_dict.keys(),reverse=True):
    	index = ratio_dict[i]
    	if (capacity - min(capacity,weights[index])) >= 0:
    		value += min(capacity, weights[index]) * values[index] / weights[index]
    		capacity = capacity - min(capacity, weights[index])
    	
    return value


if __name__ == "__main__":
	

	n_cap = (input()).split(" ")
	n, capacity =  list(map(int, n_cap))
	values = []
	weights = []
	for i in range(n):
		weight_,value_ = list(map(int, (input()).split(" ")))
		values.append(value_)
		weights.append(weight_)

	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.10f}".format(opt_value))

