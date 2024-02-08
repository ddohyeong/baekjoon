
def solution(n):
    answer = 0
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    sum = 1
    
    cnt = 1
    while True:
        if sum >= n:
            break
        sum *= cnt
        cnt += 1
        
    if sum > n :
        cnt -= 2
    else : 
        cnt -= 1
    
    return cnt