# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    return value


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

	print(items)
	print(capacity)
	print(values)
	print(weights)



    # print("{:.10f}".format(opt_vvalues=data[2:(2 * n + 2):2]
    #                        weights=data[3:(2 * n + 2):2]
    # opt_value=get_optimal_value(capacity, weights, values)alue))
