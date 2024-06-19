def solution(str_list, ex):
    answer = ''
    
    data = [i for i in str_list if not ex in i]
    
    return answer.join(data)    
    