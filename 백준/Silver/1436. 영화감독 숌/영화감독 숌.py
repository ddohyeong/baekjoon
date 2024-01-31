import sys

input = sys.stdin.readline

n = int(input())

endNumber = 666
cnt = 0
while True:
    if '666' in str(endNumber):
        cnt += 1
        if n == cnt:
            break
    endNumber += 1

print(endNumber)
