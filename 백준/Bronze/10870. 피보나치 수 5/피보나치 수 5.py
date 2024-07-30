import sys
input = sys.stdin.readline

N = int(input())

data = [0] * (20+1)

data[0] = 0
data[1] = 1
data[2] = 1

for i in range(3, N+1):
	data[i] = data[i-2] + data[i-1]

print(data[N])