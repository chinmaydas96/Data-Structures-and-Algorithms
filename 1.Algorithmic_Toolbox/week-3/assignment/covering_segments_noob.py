# Uses python3
import sys
from collections import namedtuple

#Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort()
    points = []
    #write your code here

    n = len(segments)
    first  = set(list(range(segments[0][0],segments[0][1])))

    for i in range(n-1) :

        second = set(list(range(segments[i+1][0],segments[i+1][1])))
        int_set  = first.intersection(second)
        temp_set = {}

        if (len(int_set) == 0) or (i == (n - 2)) :


            if len(int_set) > 0:
                points.append(max(int_set))

            elif len(temp_set) > 0 :
                points.append(max(temp_set))

            elif((i != (n - 2))):
                points.append(max(first))


            else:
                points.append(max(first))
                points.append(max(second))
            
        
            temp_set = {}
            first = set(list(range(segments[i+1][0],segments[i+1][1])))

        else:
            first = int_set

        temp_set = int_set


    return points

if __name__ == '__main__':
    
    #segments = [[4,8],[1,4],[2,6],[5,7]]
    #segments = [[1, 4], [2, 6], [3, 7]]
    segments = [[0, 2], [1, 2], [1, 3], [1, 4], [2, 5], [2, 5], [3, 5], [4, 5], [5, 6], [7, 9], [8, 9], [9, 10], [10, 11], [10, 13], [12, 15], [12, 15], [14, 17], [15, 16], [17, 19], [17, 20], [22, 24], [22, 25], [23, 24], [25, 28], [26, 27], [26, 29], [28, 29], [29, 30], [29, 30], [29, 32], [30, 31], [31, 33], [32, 34], [33, 35], [34, 35], [35, 36], [35, 37], [36, 37], [36, 39], [36, 39], [38, 41], [39, 42], [40, 43], [41, 42], [41, 43], [44, 45], [44, 46], [45, 47], [48, 50], [49, 51], [49, 52], [49, 52], [51, 54], [52, 53], [52, 54], [52, 55], [54, 55], [54, 57], [55, 57], [57, 59], [57, 60], [57, 60], [58, 59], [58, 59], [58, 60], [60, 62], [62, 63], [63, 64], [63, 65], [64, 66], [65, 68], [66, 68], [66, 69], [68, 71], [69, 72], [70, 73], [73, 75], [74, 75], [75, 78], [78, 79], [78, 80], [79, 80], [79, 82], [80, 83], [81, 82], [81, 83], [82, 85], [83, 85], [83, 85], [83, 85], [84, 86], [86, 88], [86, 88], [87, 89], [89, 92], [89, 92], [91, 94], [92, 94], [93, 94], [94, 96]]

    '''
    n = int(input())
    
    for i in range(n):
        a,b = list(map(int, (input()).split(" ")))
        segments.append([a, b+1])
    '''
    points = optimal_points(segments)
    print(len(points))
    print(*points)
