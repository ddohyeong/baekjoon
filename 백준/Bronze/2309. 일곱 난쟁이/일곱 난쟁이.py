li = []

for i in range(9):
    n = int(input())
    li.append(n)
    
li.sort()

su = sum(li) - 100

flag = True

cnt = 8
while flag:
    for j in range(7,-1,-1):
        if li[cnt] + li[j] == su:
            li.remove(li[cnt])
            li.remove(li[j])
            flag = False
            break
    cnt -=1


for num in li:
    print(num)    