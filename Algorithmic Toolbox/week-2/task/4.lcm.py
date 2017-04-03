# Uses python3


no = input().split(" ")
a = int(no[0])
b = int(no[1])
assert (0 <= (a, b) <= 2 * (10 ^ 9)), "a,b out of range"
best = a * b


def gcd(a, b):
    if (a > b):
        while (b != 0):
            a, b = b, a % b
    return a


h = gcd(a, b)
sum = a
while(sum != best):
    sum = sum + h
    if(sum % a == 0) and (sum % b == 0):
        best = sum
print (sum)
