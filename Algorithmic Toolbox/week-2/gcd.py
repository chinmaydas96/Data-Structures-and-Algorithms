# Uses python3


def gcd(a, b):
    best = 1
    for i in range(2, a + b):
        if(a % i == 0 and b % i == 0):
            best = i
    return best


a, b = input().split(" ")
a = int(a)
b = int(b)
assert (0 <= (a, b) <= 2 * (10 ^ 9)), "a,b should be >= 0"
print(gcd(a, b))
