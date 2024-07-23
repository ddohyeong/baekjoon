def solution(chicken):
    answer = -1
    
    coupon = 10
    answer = 0
    service = 0
    while chicken >= coupon:
        service = chicken // coupon
        chicken = service + (chicken % coupon)
        answer += service
    
    
    return answer