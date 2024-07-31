from collections import deque

N, K = map(int, input().split())

if N == K :
	print(0)
	exit()

visited = [0] * (2 * 100_000)

ans = []
def bfs():
	queue = deque()
	queue.append(N)

	while queue:
		x = queue.popleft()

		if x == K:
			return visited[K]

		for i in range(3):
			if i == 0 and  0 <= x - 1 <= 100_000 and not visited[x-1]:
				queue.append(x-1)
				visited[x-1] = visited[x] + 1

			if i == 1 and 0 <= x + 1 <= 100_000  and not visited[x+1]:
				queue.append(x+1)
				visited[x+1] = visited[x] + 1

			if i == 2 and 0 <= x * 2 <= 100_000  and not visited[x * 2]:
				queue.append(x * 2)
				visited[x * 2] = visited[x] + 1


print(bfs())

