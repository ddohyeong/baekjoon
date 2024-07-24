

def solution(babbling):
    answer = 0
    
    data = ["aya", "ye", "woo", "ma"]
    
    for s in babbling:
        tmp = s
        for i in data:
            s = s.replace(i, ' ')

        # s = s.replace(' ', '')    
        s = s.strip()
        
        if s != '':
            print(tmp)
            continue
        
        answer += 1
        
    
    return answer