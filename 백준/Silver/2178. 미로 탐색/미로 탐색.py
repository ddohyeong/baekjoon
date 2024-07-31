from collections import deque

import sys 

N, M = map(int, input().split())

data = []
for _ in range(N):
	line = input()
	data.append([int(i) for i in line])

visited = [[ False for i in range(M)]for i in range(N)]

def bfs():
    queue = deque()
    queue.append((0,0))

    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        # 동 서 남 북
       	dx = [0,0,-1,1]
       	dy = [1,-1,0,0]

       	for i in range(4):
       		nx = x + dx[i]
       		ny = y + dy[i]

       		if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 1 and visited[nx][ny] == False:
       			queue.append((nx, ny))
       			data[nx][ny] = data[x][y] + 1

    print(data[N-1][M-1])

bfs()