choose = []
mo = ['a','e','i','o','u']
def combination(data,index, level,L,C):
	if level == L:
		mos = []
		unmos = []
		for u in choose:
			if u in mo:
				mos.append(u)
			else:
				unmos.append(u)
		if len(mos) >= 1 and len(unmos) >= 2:
			print(''.join(list(map(str, choose))))

		return

	for i in range(index, C):
		choose.append(data[i])
		combination(data, i+1, level+1, L,C)
		choose.pop()

L, C = map(int, input().split())
data = input().split()

data.sort()

combination(data, 0,0,L,C)	