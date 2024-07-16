def solution(n):
    answer = 0
    
    data = 1
    
    while data ** 2 <= n :
        if data ** 2 == n :
            return 1
        data += 1
    
    return 2