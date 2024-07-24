def str_push(data):
    return data[len(data) - 1] + data[:len(data) - 1]


def solution(A, B):
    answer = 0
    
    while answer < len(A):
        if A == B:
            return answer
        A = str_push(A)
        answer += 1
        
    return -1
    
    
    return answer