# Uses python3


def get_change(m):
    # write your code here
    money = 0
    count = 0
    coin = [10, 5, 1]

    for i in range(0, 3):
        while(money + coin[i] <= m):
            money += coin[i]
            count += 1
    return count


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
