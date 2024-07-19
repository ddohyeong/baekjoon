def solution(num_list, n):
    answer = []
    
    
    data = []
    for i in range(len(num_list)):
        data.append(num_list[i])
        if (i+1) % n == 0 :
            answer.append(data)
            data = []
        
    
    return answer