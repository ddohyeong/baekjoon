T = int(input())
arrays = []
for _ in range(T):
    row = list(input().split())
    arrays.append(row)
for arr in arrays:
    n = float(arr[0])
    for i in range(1,len(arr)):
        if arr[i] == '@':
            n *= 3.0
        if arr[i] =='%':
            n += 5.0
        if arr[i] == '#':
            n -= 7.0
    print('{:.2f}'.format(n))