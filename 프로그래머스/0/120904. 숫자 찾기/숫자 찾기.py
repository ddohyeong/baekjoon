def solution(num, k):
    answer = 0
    data= str(num)
    d = str(k)
    try:
        return data.index(d) + 1
    except ValueError:
        return -1
    
