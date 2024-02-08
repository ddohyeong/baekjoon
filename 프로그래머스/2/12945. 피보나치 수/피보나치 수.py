def solution(n):
    answer = 0
    
    f = [0] * (n+1)
    
    f[0] = 0
    f[1] = 1
    f[2] = 1
    
    for i in range(3,n+1):
        f[i] = f[i-2] + f[i-1]
    
    answer = f[n] % 1234567
    print(answer)
    return answer
