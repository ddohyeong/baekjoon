def solution(cipher, code):
    answer = ''
    n = 1
    
    s = len(cipher) // code 
    
    for i in range(1,s+1):
        answer += cipher[code * i - 1]
    
    return answer