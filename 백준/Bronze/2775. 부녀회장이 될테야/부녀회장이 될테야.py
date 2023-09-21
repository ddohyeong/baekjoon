import sys
input = sys.stdin.readline

data = []

check = []
max_n = 0
max_k = 0
T = int(input())
for _ in range(T):
    n = int(input())
    k = int(input())
    check.append([n,k])
    if n > max_n:
        max_n = n
    if k > max_k:
        max_k = k

first = [i for i in range(0,max_k+1)]
data.append(first)
for _ in range(max_n):
    data.append([0] * (max_k+1))

for i in range(1, max_n+1):
    for j in range(1, max_k +1):
        data[i][j] = sum(data[i-1][y] for y in range(j+1))


for d in check :
    print(data[d[0]][d[1]])
