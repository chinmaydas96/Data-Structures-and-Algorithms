# Uses python3

def fib(n):
    old = 0
    new = 1
    if(n >= 2):
        for i in range(2, n + 1):
            new, old = new + old, new

        return new
    else:
        return n


n = int(input())
# assert ((n >= 0) and (n <= 45)), "n should be in range 0 ≤ n ≤ 45"
print(fib(n))
