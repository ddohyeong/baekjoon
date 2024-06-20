def solution(my_string):
    answer = ''
    
    #32
    
    for i in my_string:
        if ord('a') <= ord(i) and ord(i) <= ord('z'):
            answer += (chr(ord(i) - 32))
        else:
            answer += (chr(ord(i) + 32))
                       
        
        
        
        
    return answer