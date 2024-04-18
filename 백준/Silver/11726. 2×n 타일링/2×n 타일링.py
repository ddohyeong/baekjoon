s = int(input())

data = []

data.append(0)
data.append(1)
data.append(2)

for i in range(3, s+1):
    data.append(data[i-1] + data[i-2])

print(data[s] % 10_007)