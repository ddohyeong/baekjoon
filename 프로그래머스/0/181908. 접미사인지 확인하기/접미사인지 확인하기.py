def solution(my_string, is_suffix):
    answer = 0
    
    my = my_string[::-1]
    suffix = is_suffix[::-1]
    
    if my[:len(is_suffix)] == suffix:
        answer = 1
        
    
    return answer