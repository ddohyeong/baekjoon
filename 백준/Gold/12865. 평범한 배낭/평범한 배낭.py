# top-down
def func(n, k):
	global W,V,dp

	# base case:
	if n == 0 or k == 0:
		return 0

	if dp[n][k] != -1:
		return dp[n][k]

	# recursive case
	dp[n][k] = func(n-1, k)
	if k - W[n] >= 0:
		dp[n][k] = max(func(n-1, k), func(n-1, k-W[n]) + V[n])

	return dp[n][k]



N, K = map(int, input().split())

W, V = [0], [0]

for _ in range(N):
	w,v = map(int, input().split())

	W.append(w)
	V.append(v)

dp = [[-1] * (K+1) for _ in range(N + 1)]

print(func(N,K))
