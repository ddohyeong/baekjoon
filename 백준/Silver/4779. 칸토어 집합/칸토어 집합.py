import sys
input = sys.stdin.readline

def fun1(line):
	if len(line) == 1:
		return '-'
	
	slice_line = len(line) // 3

	return fun1(line[0:slice_line]) + ' ' * slice_line  + fun1(line[(slice_line*2):])

data = []

while True:

	line = input()
	if line == "":
		break
	data.append(int(line))

for N in data:

	if N == 0:
		print('-')
		continue

	ans = '-' * (3 ** N)

	print(fun1(ans))

