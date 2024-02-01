# bfs
from collections import deque

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

# 양방향 그래프
for i in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs(graph, start, visited):
    cnt = 0
    queue = deque([start])  # 큐를 구현하기 위해서 deque라이브러리 사용
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt +=1 
    print(cnt)


bfs(graph, 1, visited)


