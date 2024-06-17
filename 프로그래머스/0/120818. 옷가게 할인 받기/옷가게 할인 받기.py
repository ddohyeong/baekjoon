def solution(price):
    answer = 0
    
    data = [(500_000,0.2), (300_000,0.1), (100_000,0.05), (0,0)]
    
    for key, value in data:
        if price >= key:
            answer = price - (price * value)
            return int(answer)
            
        
    
    # return answer