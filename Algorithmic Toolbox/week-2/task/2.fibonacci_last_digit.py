# Uses python3


def fib(n):
    old = 0
    new = 1
    if(n >= 2):
        for i in range(2, n + 1):
            new, old = new + old, new

    return new


n = int(input())
assert (n >= 0 and n <= 10 ^ 7), "n should be in range 0 ≤ n ≤ 10^7 "
print(fib(n) % 10)
