def solution(n):
    answer = 0
    data = 1
    
    while data <= n:
        if n % data == 0:
            answer += 1

        data += 1
    
    return answer


