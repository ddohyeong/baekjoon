import sys
input = sys.stdin.readline

N = 1000 - int(input())


def count_coin(N):

    coin_list = [500,100,50,10,5,1]

    count = 0
    for coin in coin_list:
        count  += N//coin
        N %= coin

    return count


print(count_coin(N))

