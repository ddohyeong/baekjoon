from itertools import permutations

def fact(n):
	if n == 0 :
		return 1
	return fact(n-1) * n


s = input()
ans = 0
for perm in permutations(s):
	ok = True

	for i in range(len(s)-1):
		if perm[i] == perm[i+1]:
			ok = False
	ans += ok

for i in range(ord('a'), ord('z')+1):
	ans //= fact(s.count(chr(i)))


print(ans)

