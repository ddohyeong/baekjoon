N, M = map(int, input().split())

infos = list(map(int, input().split()))

minus = []
plus = []
max = 0 
for i in infos:
	if abs(i) > abs(max):
		max = i
	if i > 0:
		plus.append(i)
	else:
		minus.append(i)

minus.sort()
plus.sort(reverse = True)

ans = 0
for i in range(0,len(minus),M):
	ans += -2 * minus[i]

for i in range(0,len(plus),M):
	ans += 2 * plus[i]

if max > 0 :
	ans -= max
else:
	ans += max

print(ans)
