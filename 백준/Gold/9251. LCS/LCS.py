s1 = [0] + list(input())
s2 = [0] + list(input())

dp = [[0] * (len(s2)) for _ in range(len(s1))]

N = len(s1)
M = len(s2)

for i in range(1,N):
	for j in range(1,M):
		if s1[i] == s2[j]:
			dp[i][j] = dp[i-1][j-1] + 1

		else: 
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N-1][M-1])