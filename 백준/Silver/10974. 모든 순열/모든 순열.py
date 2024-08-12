N = int(input())
check = [False] * N
lst = [1,2,3,4,5,6,7,8]

choose = []
def permutation(level):
	if level == N:
		for u in choose:
			print(u, end = ' ')
		print()
		return 
	
	for i in range(N):
		if check[i] == True:
			continue

		choose.append(lst[i])
		check[i] = True

		permutation(level+1)

		check[i] = False
		choose.pop()


permutation(0)
