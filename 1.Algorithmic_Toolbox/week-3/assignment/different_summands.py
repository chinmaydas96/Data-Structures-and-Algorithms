# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    list_no = list(range(n))
    

    return list_no

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
