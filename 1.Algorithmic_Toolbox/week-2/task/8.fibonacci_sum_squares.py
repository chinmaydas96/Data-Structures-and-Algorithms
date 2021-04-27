# Uses python3

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


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    vertical = get_fibonaccihuge(n, 10)
    horizontal = vertical + get_fibonaccihuge(n-1, 10)
    # print(vertical , horizontal)
    return (vertical * horizontal) % 10


if __name__ == '__main__':
    number = int(input())
    print(fibonacci_sum_squares_naive(number))
