# Uses python3


def largest_number(a):
    res = ""
    i = 0
    while len(a) > 0:
        i = i + 1
        sMax = find_safe_max_number(a)
        res += sMax
        a.remove(sMax)

    return res


def find_safe_max_number(a):
    max_ = a[0]
    for x in a:
        max_ = safe_max(max_, x)
    return max_


def safe_max(max_, x):
    A = str(max_) + str(x)
    B = str(x) + str(max_)
    if (A > B):
        return max_
    else:
        return x


if __name__ == '__main__':
    n = int(input())
    data = [str(x) for x in input().split()]
    print(largest_number(data))
