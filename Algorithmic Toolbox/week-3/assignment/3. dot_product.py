# Uses python3

import sys


def max_dot_product(a, b, n):
    # write your code here

    res = 0
    for i in range(len(a)):
        max_a = max_index(a)
        max_b = max_index(b)    
        res += a[max_a] * b[max_b]
        # print (res)
        del a[max_a]
        del b[max_b]

    return res

def max_index(array):
    max = array[0]
    index = 0
    for i in range(len(array)):
        if (array[i] > max):
            max = array[i] 
            index = i 
            
    return index            
if __name__ == '__main__':

    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    print(max_dot_product(a, b, n))
    # print (max_index(a))