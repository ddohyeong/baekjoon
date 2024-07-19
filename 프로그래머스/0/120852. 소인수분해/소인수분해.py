def solution(n):
    answer = set()
    
    check = 2
    
    while n > 1 :
        if n % check == 0:
            n /= check
            answer.add(check)
            
        else:
            check +=1 
            
        
    
    return sorted(list(answer))