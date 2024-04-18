# N 값 받기 
s = int(input())

# 리스트 선언
data = []

# 인덱스 0,1,2 에 해당하는 값 초기 지정
data.append(0)
data.append(1)
data.append(3)


# 동적 프로그래밍 함수
for i in range(3, s+1):
    data.append(data[i-1] + data[i-2] * 2)

print(data[s] % 10_007)