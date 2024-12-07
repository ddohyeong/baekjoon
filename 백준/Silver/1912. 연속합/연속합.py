N = int(input())	

data = [0] + list(map(int, input().split()))

dp = [-100000000000 for i in range(N+1)]

dp[1] = data[1]


prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + data[i - 1]

m = 1
for n in range(2, N+1):
	dp[n] = max(dp[n-1], prefix_sum[n] - prefix_sum[m] + data[n], data[n])

	if prefix_sum[n] - prefix_sum[m] + data[n] < data[n]:
		m = n


print(max(dp))

