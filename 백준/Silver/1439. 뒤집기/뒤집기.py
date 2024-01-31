s = input()

cnt = 0

oneCount = 0
zeroCount = 0

i = 0
j = 0
while i < len(s):
    if s[i] == '0':
        zeroCount += 1
        # 현재 '0' 뒤에 연속적으로 나오는 '0'들을 건너뛰기
        while i < len(s) and s[i] == '0':
            i += 1
    else:
        i += 1

while j < len(s):
    if s[j] == '1':
        oneCount += 1
        # 현재 '0' 뒤에 연속적으로 나오는 '0'들을 건너뛰기
        while j < len(s) and s[j] == '1':
            j += 1
    else:
        j += 1

print(min(zeroCount, oneCount))
