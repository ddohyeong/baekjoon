def solution(dot):
    answer = 0
    data = []
    sol = [[True, True],[False, True],[False, False],[True, False]]
    data.append(True if dot[0] > 0 else False)
    data.append(True if dot[1] > 0 else False)
    
    return sol.index(data) + 1 