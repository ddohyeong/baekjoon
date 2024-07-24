def solution(numlist, n):
    answer = []
    
    data = []
    
    for i in numlist:
        data.append([abs(i - n),i])
        
    data.sort(key = lambda x : (x[0], -x[1]))

    return [i[1] for i in data]
