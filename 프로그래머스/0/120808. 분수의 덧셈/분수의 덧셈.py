import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    a = (numer1 * denom2) + (numer2 * denom1)
    u = denom1 * denom2
    
    gcd_result =math.gcd(a,u)
    
    print([a//gcd_result, u// gcd_result])
    
    return [a//gcd_result, u// gcd_result]