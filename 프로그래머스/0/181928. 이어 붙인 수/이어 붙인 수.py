def solution(num_list):
    answer = 0
    
    even = [str(i) for i in num_list if i % 2 == 0]
    odd = [str(i) for i in num_list if i % 2 != 0]
    
    
    return int(''.join(even)) + int(''.join(odd)) 
    
    # return int(''.join(even)) + int(''.join(odd))