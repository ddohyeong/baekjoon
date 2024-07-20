

# def fact(n):
#     data = [1]
    
#     sum = 1
#     for i in range(1, n+1):
#         sum *= i
#         data.append(sum)
    
#     return data
    
    

# def solution(balls, share):
#     answer = 0
    
#     data = fact(balls)
#     print(data)
    
    
#     answer = data[balls] // (data[balls - share] * data[share])
    
    
    
#     return answer
import math
def solution(balls, share):
    answer = 0
    return math.comb(balls, share)