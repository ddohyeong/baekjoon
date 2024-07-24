def solution(quiz):
    answer = []
    
    for i in quiz:
        data = i.split(' ')
        
        ans = 0
        
        X = int(data[0])
        Y = int(data[2])
        
        if data[1] == '-':
            ans = X - Y
        else:
            ans = X + Y
        
        if ans == int(data[4]):
            answer.append('O')
        else:
            answer.append('X')
            
            
    
    return answer