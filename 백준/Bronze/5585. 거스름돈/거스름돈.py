lst = [500, 100, 50, 10, 5, 1]
money = 1000 -  int(input())

sum = 0 
for i in lst:
	if money < i :
		continue

	sum += money // i
	money = money % i

print(sum)




