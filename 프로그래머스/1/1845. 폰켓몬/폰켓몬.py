from itertools import combinations

def solution(nums):
    answer = 0
    
    data = list(set(nums))
    
    length = len(nums) // 2
    
    if len(data) > length :
        answer = length 
    else : 
        answer = len(data)
    
    return answer