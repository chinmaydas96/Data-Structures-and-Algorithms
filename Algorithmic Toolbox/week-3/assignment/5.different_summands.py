# Uses python3


def optimal_summands(n):
    summands = []

    if (n <= 2):
        summands.append(n)
    else:
        l = 1
        while (n > 2 * l):
            summands.append(l)
            n -= l
            l += 1
        summands.append(n)    
    return summands


if __name__ == '__main__':
    number = int(input())
    summands = optimal_summands(number)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
