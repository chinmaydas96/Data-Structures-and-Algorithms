# Uses python3


from collections import namedtuple


Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    # write your code here

    segments = sorted(segments, key=lambda segment: segment.end)
    current = segments[0].end
    points.append(current)

    for s in segments:
        if((current < s.start) or (current > s.end)):
            current = s.end
            points.append(current)

    return points


if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        m = input().split(" ")
        data.append(int(m[0]))
        data.append(int(m[1]))

    segments = list(map(lambda x: Segment(
        x[0], x[1]), zip(data[::2], data[1::2])))

    points = optimal_points(segments) print(len(points)) for p in points:
    print(p, end=' ')
