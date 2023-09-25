import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
max_num=max(li)
avg = []
for i in li:
    avg.append(i / max_num * 100)

print(sum(avg)/ n)
    
