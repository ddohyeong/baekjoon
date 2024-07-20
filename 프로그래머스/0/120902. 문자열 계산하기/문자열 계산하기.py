def solution(my_string):
    answer = 0
    
    data = my_string.split(" ")
    
    
    answer = int(data[0]) 
    for i in range(2, len(data),2):
        if data[i-1] == '+':
            answer += int(data[i])
        if data[i-1] == '-':
            answer -= int(data[i])
    
    
    return answer