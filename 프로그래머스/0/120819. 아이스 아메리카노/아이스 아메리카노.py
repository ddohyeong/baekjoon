def solution(money):
    answer = []
    americano = 5500
    
    answer.append(money // 5500)
    answer.append(money % 5500)
    
    return answer