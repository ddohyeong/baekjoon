import sys
N  = int(input())
data = set([])

for _ in range(N):
    data.add(input())

list_data = list(data)
# list_data.sort()
list_data.sort(key=lambda x: (len(x), x))
print('\n'.join(list_data))