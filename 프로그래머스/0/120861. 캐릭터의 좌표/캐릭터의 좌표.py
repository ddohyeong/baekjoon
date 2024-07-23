def solution(keyinput, board):

    # up, down, left, right
    direct = {
        'up' : (0,1),
        'down' : (0,-1),
        'left' : (-1,0),
        'right' : (1,0)
    }
    
    
    x ,y = 0,0
    
    for i in keyinput:
        x += direct[i][0]
        y += direct[i][1]
        
        if -(board[0] // 2) > x or x > (board[0] // 2):
            if x > 0: 
                x = board[0] // 2
            else:
                x = -(board[0]//2)
            
        if -(board[1] // 2) > y or y > (board[1] // 2):
            if y > 0: 
                y = board[1] // 2
            else:
                y = -(board[1]//2)
        
        
    
    answer = [x,y]
    
    return answer