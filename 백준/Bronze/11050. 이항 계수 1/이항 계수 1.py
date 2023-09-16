import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if K == 0 or K == N :
    print(1)
    exit()



data = []
sum  = 1
for i in range(1,N+1):
    sum *= i
    data.append(sum)
    

print(data[N-1] // (data[K-1] * data[N - K -1]))

