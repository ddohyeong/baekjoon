import sys
input = sys.stdin.readline

N = int(input())

count = 0
for i in range(1,N+1):
    data = i
    if i % 5 == 0:
        while True:
            if data % 5 == 0:
                count +=1
                data //= 5
            else:
                break
print(count)