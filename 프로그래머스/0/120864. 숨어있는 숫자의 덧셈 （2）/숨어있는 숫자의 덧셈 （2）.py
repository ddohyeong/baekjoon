def solution(my_string):
    my_string += 'a';
    answer = 0
    dt = ''
    
    for i in my_string:
        if i.isdigit():             
            dt += i
            continue
        
        if dt != '':
            answer += int(dt)
        dt = ''
                
    
    return answer