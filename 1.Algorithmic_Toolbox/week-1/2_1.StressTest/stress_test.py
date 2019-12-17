import random

def max_pairwise_product_fast(n, a):
    global fast
    max_index1 = -1
    for i in range(n):
      if max_index1 == -1 or a[i] > a[max_index1]:
          max_index1 = i

    max_index2 = -1
    for i in range(n):
      if i != max_index1 and (max_index2 == -1 or a[i] > a[max_index2]):
          max_index2 = i
    fast = a[max_index1] * a[max_index2]
    return fast

def max_pairwise_product(n, a):
    global result
    for i in range(0, n):
        for j in range(i + 1, n):
            if a[i] * a[j] > result:
                result = a[i] * a[j]
                print(i,j)

    return result


def max_pairwise_optimize(n, a):
    max1 = 0
    max2 = 0

    for i in range(0, n):
        if a[i] > max1 or a[i] > max2:
            max1 = max(max1, max2)
            max2 = a[i]

    return max1 * max2            



result1 = 0
fast1 = 0


while result1 == fast1:
    if __name__ == '__main__':
        result = 0
        fast = 0
        n = (random.randint(2, 11))
        a = list(random.randint(0, 99999) for r in range(n))
        assert (len(a) == n)
        result1 = max_pairwise_product(n, a)


        fast1=max_pairwise_optimize(n, a)
        print('Optimized :',fast1, ', Naive : ',result1, "OK")
    else:
        print("Wrong Answer")
print('Wrong answer : ',a)