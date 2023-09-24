import sys
input =sys.stdin.readline

N,M = map(int,input().split())

inp = list(map(int, input().split()))

inp.sort(reverse=True)

count = 0
sum = 0
data = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum = inp[i] + inp[j]+inp[k]
            if M >= sum:
                data.append(sum)
data.sort()
print(data[-1])
