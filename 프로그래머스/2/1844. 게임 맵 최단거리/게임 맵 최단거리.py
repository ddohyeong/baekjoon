from collections import deque


def solution(maps):
    answer = 0
    # down up right left
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    n, m = len(maps), len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    queue = deque()
    queue.append([0,0])
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if maps[nx][ny] == 0:
                continue
                
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                
                queue.append([nx,ny])
    
    print(maps[n-1][m-1])
    
    answer = maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1
    return answer