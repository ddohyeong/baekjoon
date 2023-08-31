i = 0
lists = []

def move(first,end):
    global i
    i +=1
    lists.append([first,end])

def hanoi(n,first,mid,end):
    if n == 0:
        return
    else:
        hanoi(n-1,first,end,mid)
        move(first,end)
        hanoi(n-1,mid,first,end)

num = int(input())


hanoi(num,'1','2','3')

print(i)
for i in lists:
    print(i[0],i[1])