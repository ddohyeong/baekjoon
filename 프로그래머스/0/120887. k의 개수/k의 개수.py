def solution(i, j, k):
    
    return sum([str(data).count(str(k)) for data in range(i,j+1)])