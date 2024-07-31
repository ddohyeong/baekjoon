import sys
input = sys.stdin.readline

N,K = map(int,input().split())

data = []
data.append([0,0])
for _ in range(N):
	data.append(list(map(int,input().split())))

dp =[[ 0 for _ in range(K+1)] for _ in range(N+1)]



for i in range(1,N+1):
	for j in range(1, K+1):
		
		dp[i][j] = dp[i-1][j]
		
		if j - data[i][0] >= 0:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j - data[i][0]] + data[i][1])


print(dp[N][K])