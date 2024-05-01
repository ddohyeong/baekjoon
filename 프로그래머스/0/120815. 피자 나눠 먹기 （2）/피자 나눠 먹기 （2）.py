import math

def lcm(a, b):
    return a * b / math.gcd(a, b)

def solution(n):
    answer = 0
    
    
    if n % 6 == 0:
        return n//6
    else:
        return lcm(n,6) // 6
    
    return answer