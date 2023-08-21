N = int(input())
arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

dp = [N * [0] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if(dp[i][j] == 0 or (i == N-1 and j== N-1)):
            continue
        if(i+arr[i][j] < N): 
            dp[i+arr[i][j]][j] += dp[i][j]
        if(j+arr[i][j] < N ):
            dp[i][j+arr[i][j]] += dp[i][j]
            
print(dp[-1][-1])
