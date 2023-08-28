s = input()
dicts = ['c=','c-','dz=','d-','lj','nj','s=','z=']

check = 0

for i in dicts:
    f= s.find(i)
    if f > -1:
        s=s.replace(i," ")

print(len(s))