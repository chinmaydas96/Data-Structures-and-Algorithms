# python3
import sys


def compute_min_refills(distance, tank , n  , stops):


    # write your code here
    no_of_refills = 0
    current_stop = 0
    
    stops.insert(0, 0)
    stops.insert(len(stops), distance)

    while(current_stop <= n):
        last_refill = current_stop

        while(current_stop <= n) and (stops[current_stop+1] - stops[last_refill] <= tank):
            current_stop += 1
        if current_stop == last_refill:
            return -1
        if current_stop <= n:
            no_of_refills += 1
    return no_of_refills
            

if __name__ == '__main__':

    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, (input()).split(" ")))

    print(compute_min_refills(d, m, n, stops))
