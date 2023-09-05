string=input()
bomb = input()

stack = []

for c in string:
    stack.append(c)
    if c == stack[-1] and ''.join(stack[-len(bomb) : ]) == bomb:
        del stack[-len(bomb) : ]

ans = ''.join(stack)
if len(ans) != 0:
    print(ans)
else:
    print('FRULA')