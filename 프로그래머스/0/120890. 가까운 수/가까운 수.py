def solution(array, n):
    answer = 0
    
    data = []
    
    return sorted(array, key = lambda x : (abs(n-x), x))[0]

# sorted(array, key = lambda x : (abs(n-x), x))