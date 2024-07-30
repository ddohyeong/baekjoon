money = int(input())

change_money = [500, 100,50,10,5,1]

change =1000 - money

ch = 0
for i in change_money:
	ch += change // i 
	change = change % i

print(ch)
