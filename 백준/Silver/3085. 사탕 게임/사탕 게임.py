import copy
N = int(input())

data = [list(input()) for _ in range(N)]


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우


# 연속적인 문자열 제일 긴거
def sol(arr):
	t = [0]
	c = 1
	for i in range(1, len(arr)):
		if arr[i-1] == arr[i]:
			c += 1
		else:
			t.append(c)
			c = 1

	t.append(c)	
	return max(t)

ans = []
for x in range(N):

	ans.append(sol(data[x]))
	ans.append(sol([row[x] for row in data]))

	for y in range(N):
		for dx,dy in directions:
			nx, ny = x + dx, y + dy

			if 0 <= nx <N and 0<= ny <N:
				count = [0]
				temp = copy.deepcopy(data)

				if data[x][y] != data[nx][ny]:
					temp[x][y],temp[nx][ny] = temp[nx][ny], temp[x][y]
					
					count.append(sol(temp[nx]))
					count.append(sol([row[ny] for row in temp]))

				ans.append(max(count))


print(max(ans))

