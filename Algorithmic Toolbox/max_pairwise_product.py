# import pdb
n = int(input())
a = [int(x) for x in input().split()]
assert (len(a) == n)
high = 0
for i in range(0, n):
    for k in range(i + 1, n):
        if (a[i] * a[k] > high):
            high = a[i] * a[k]
            # pdb.set_trace()

print(high)
