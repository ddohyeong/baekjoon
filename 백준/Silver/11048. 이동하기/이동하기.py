N,M = map(int, input().split())

data = []
data.append([0] * (M+1))
for _ in range(N):
	data.append([0] + list(map(int, input().split())))

dp = [[0] * (M+1) for _ in range(N+1)]


for i in range(1,N+1):
	for j in range(1,M+1):
		data[i][j] = max(data[i-1][j], data[i][j-1]) + data[i][j]

print(data[N][M])