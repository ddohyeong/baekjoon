def solution(dots):
    answer = 0
    
    
    
    # y2 - y1 / x2 - x1
    # y4 - y3 / x4 - x3
    
    l = [2,3,4]
    
    
    try:
        for i in range(1,4):
            a,b = 0,0
            
            tmp = [1,2,3]
            tmp.pop(tmp.index(i))
            print(tmp)
            
            a = (dots[i][1] - dots[0][1]) / (dots[i][0] - dots[0][0])
            b = (dots[tmp[0]][1] - dots[tmp[1]][1]) / (dots[tmp[0]][0] - dots[tmp[1]][0])

            
            print(a,b)
            
            if a == b:
                return 1
    except:
        pass
    
    return 0
    
    
    return answer