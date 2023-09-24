import sys
# input = sys.stdin.readline

T = int(input())

def fun(data):
    stk = []
    isFlag = False
    for i in data:
        if i == '(':
            stk.append(i)
        else:
            if len(stk) > 0:
                if stk.pop() != '(':
                    isFlag = True
                    break
            else : 
                isFlag = True
    if len(stk) > 0:
        isFlag = True

    if isFlag:
        print("NO")
    else:
        print("YES")

for _ in range(T):
    fun(input())
