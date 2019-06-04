# Uses python3


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    # For proper division output use '//'
    return int(a * b) // int(gcd(a, b))


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(int(lcm(a, b)))
