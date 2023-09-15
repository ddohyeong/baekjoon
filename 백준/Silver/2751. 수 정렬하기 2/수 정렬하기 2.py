import sys 
input = sys.stdin.readline

# data = set([])
# print(list(data))

N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

data.sort()

for i in data:
    print(i)