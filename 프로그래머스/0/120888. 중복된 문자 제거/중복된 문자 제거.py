def solution(my_string):
    answer = ''
    
    answer = []
    
    for i in my_string:
        if i in answer:
            continue
        
        answer.append(i)
    
    return ''.join(answer)