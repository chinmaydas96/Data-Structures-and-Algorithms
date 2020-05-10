# python3
import sys


def compute_min_refills(distance, tank , n  , stops):
    # write your code here
	no_of_refills = 0
	intial_stop = 0
	current_stop = 0
	stops.insert(len(stops) + 1, distance)


	for i in stops:
		current_stop = i
		if current_stop - intial_stop < tank:
			continue
		no_of_refills += 1
		intial_stop = i

	print(intial_stop)
	if intial_stop == stops[-1]:
		return no_of_refills
	else:
		return -1


if __name__ == '__main__':

    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, (input()).split(" ")))

    print(compute_min_refills(d, m, n, stops))
