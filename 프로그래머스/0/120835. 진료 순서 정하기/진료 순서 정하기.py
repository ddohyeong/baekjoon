def solution(emergency):
    answer = []
    
    data = sorted(emergency) # 정렬된 값
    check = [i for i in range(len(data),0,-1)] 
    
    key = dict(zip(data, check))    
    
    for i in emergency:
        answer.append(key.pop(i))
    
    return answer