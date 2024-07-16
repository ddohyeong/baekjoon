def solution(n, numlist):
    answer = []
    
    data = [i for i in numlist if i % n == 0]
    print(data)
    
    return data