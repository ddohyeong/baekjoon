from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])  # 큐를 구현하기 위해서 deque라이브러리 사용
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]: 
                queue.append(i)
                visited[i] = True


N,M,V = map(int, input().split())

graphs = [[] for _ in range(N+1)]

inp_data = []
for i in range(M):
    inp_data.append( list(map(int, input().split())))

inp_data.sort()

for i in inp_data:
    graphs[i[0]].append(i[1])
    graphs[i[1]].append(i[0])

for i in graphs:
    i.sort()

visited = [False] * (N+1)
dfs(graphs, V, visited)
visited = [False] * (N+1)
print()
bfs(graphs, V, visited)
