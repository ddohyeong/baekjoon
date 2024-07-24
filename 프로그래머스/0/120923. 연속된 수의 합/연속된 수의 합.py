def solution(num, total):
    answer = [0] * num
    
    data = total // num
            
    if num % 2 == 0:
        idx = num // 2 - 1
    else:
        idx = num // 2
    answer[idx] = data

    sums = 1
    for i in range(idx+1, num):
        answer[i] = data + sums
        sums += 1
    minus = -1

    for j in range(idx-1, 0-1, -1):
        answer[j] = data + minus
        minus -= 1
            
    
         
    
    return answer