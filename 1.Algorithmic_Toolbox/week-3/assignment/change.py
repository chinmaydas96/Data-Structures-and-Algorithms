# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [10, 5, 1]
    total_coins = 0

    for coin in coins:
    	while m >= coin :
    		m -= coin
    		total_coins += 1

    return total_coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
