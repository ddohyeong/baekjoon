def solution(lines):
    answer = 0
    
    arr = [0] * 201
    
    for line in lines:
        for i in range(100+line[0],100+line[1],1):
            arr[i] += 1

    print(arr)
            
    for i in arr:
        if i > 1:
            answer += 1
    
    return answer