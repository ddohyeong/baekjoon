from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    temp = []
    
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        temp.append(v)
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    temp.sort()
    return temp

def solution(n, computers):
    answer = 0
    graph = [[]]
    for i in range(n):
        t = []
        for j in range(n):
            if i == j :
                continue
            if computers[i][j] == 1:
                t.append(j+1)
        graph.append(t)

    # a = [[], [2],[1],[]]
    # b =[[], [2],[1,3],[2]]
    arr = []
    for i in range(1,n+1):
        visited = [False] * (n + 1)
        arr.append(bfs(graph, i, visited))
        print()

    li = list(set([tuple(set(item)) for item in arr ]))
    answer = len(li)
    return answer