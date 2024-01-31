import sys

input = sys.stdin.readline

n, m = map(int, input().split())

brands = []

for _ in range(m):
    brands.append(list(map(int, input().split())))

brands.sort(key=lambda x: x[0])
packPrice = brands[0][0]
brands.sort(key=lambda x: x[1])
eachPrice = brands[0][1]

packCount = n // 6
eachCount = n % 6
each2 = 9999999999
if eachCount > 0:
    pack = packPrice * (packCount + 1)
    each = packPrice * packCount + eachPrice * eachCount
    each2 = eachPrice * n
else:
    pack = packPrice * packCount
    each = n * eachPrice

print(min(pack, each, each2))
