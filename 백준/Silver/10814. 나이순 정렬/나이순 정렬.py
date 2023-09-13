N = int(input())

result = []
for i in range(N):
    data = input().split()
    new_data = [int(data[0]) , data[1] , i]
    result.append(new_data)

sort_data = sorted(result, key = lambda x: (x[0] , x[2]))

for i in sort_data:
    print(i[0], i[1])