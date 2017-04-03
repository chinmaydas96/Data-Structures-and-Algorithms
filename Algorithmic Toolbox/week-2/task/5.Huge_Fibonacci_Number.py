no = input().split(" ")
n = int(no[0])
m = int(no[1])

assert (1 <= n <= 10 ^ 18 and 2 <= m <= 10 ^ 5), "n,m out of range"


def fib(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def get_length(m):
    if m <= 1:
        return m
    index, i = 0, 0
    a, b = 0, 1
    while True:
        a, b = b, ((a + b) % m)
        if b == 1 and a == 0:
            index = i
            break
        i += 1
    return index + 1


def get_fibonaccihuge(n, m):
    length = get_length(m)
    remainder = n % length
    while n > length:
        n = remainder
        remainder = n % length

    return fib(n) % m


if __name__ == '__main__':
    print(get_fibonaccihuge(n, m))
    # print(get_fibonaccihuge(2816213588, 30524))
