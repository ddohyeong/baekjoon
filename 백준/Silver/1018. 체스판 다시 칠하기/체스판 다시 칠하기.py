import copy
N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]

t1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
t2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]


check = []
for i in range(N-8+1):
	for j in range(M-8+1):
		temp = []

		te1 = copy.deepcopy(data)
		te2 = copy.deepcopy(data)
		cnt1 = 0
		cnt2 = 0
		for x in range(i,i+8):
			for y in range(j,j+8):
				if te1[x][y] != t1[x-i][y-j]:
					# if te1[x][y] == 'B':
					# 	te1[x][y] = 'W'
					# else:
					# 	te1[x][y] = 'B'
					cnt1 += 1
				if te2[x][y] != t2[x-i][y-j]:
					# if te2[x][y] == 'B':
					# 	te2[x][y] = 'W'
					# else:
					# 	te2[x][y] = 'B'
					cnt2 += 1
	
		check.append(min(cnt1, cnt2))

print(min(check))


						



