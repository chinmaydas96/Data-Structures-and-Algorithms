# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    high = n
    low = 1

    while (high > 0):

    	if (high <= 2 * low ):
    		summands.append(high)
    		high -= high
    	else:
    		summands.append(low)
    		high -= low
    	low += 1


    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
