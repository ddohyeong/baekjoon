import sys
input = sys.stdin.readline

N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

data.sort(key= lambda x : (x[0], x[1]))

for i in data:
    print(i[0],i[1])