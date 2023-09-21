import sys
input = sys.stdin.readline

N = int(input())
inp = list(map( int,input().split()))

count = 0
for data in inp:
    if data == 1:
        continue
    if data == 2:
        count +=1
        continue

    isFalg = False
    for i in range(2, data):
        if data % i == 0:
            isFalg = True
            break            

    if not isFalg:
        count +=1

print(count)