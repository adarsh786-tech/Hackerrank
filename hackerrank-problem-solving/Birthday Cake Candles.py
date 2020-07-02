import math


def birthday_cake_candles(ar,maximum):
    ans = 0
    for i in range(n):
        if(maximum == ar[i]):
            ans+=1
    print(ans)


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    maximum = max(ar)
    birthday_cake_candles(ar,maximum)
