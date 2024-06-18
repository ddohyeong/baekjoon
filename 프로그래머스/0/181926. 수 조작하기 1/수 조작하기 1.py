def solution(n, control):
    answer = 0
    
    data = {"w":1,"s":-1,"d":10,"a":-10}
    
    for i in control:
        n += data[i]
    
    return n