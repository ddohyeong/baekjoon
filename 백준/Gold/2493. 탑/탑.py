n = int(input())
data = list(map(int, input().split()))

stack = []
ans = [0] * n

for i in range(n):
    h = data[i]
    while stack:
        if stack[-1][0] < h:
            stack.pop()
        else:
            ans[i] = stack[-1][1] + 1
            break

    stack.append([h, i])

for s in ans:
    print(s, end=" ")
