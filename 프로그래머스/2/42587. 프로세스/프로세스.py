from collections import deque

def solution(priorities, location):
    answer = 0
    
    
    queue = [(i, item) for i, item in enumerate(priorities)]
    
    sorted_queue = sorted(queue, key=lambda x: x[1], reverse= True)

    q =  deque(queue)
    
    while q:
        id, val = q.popleft()
        
        if any(val < q[i][1] for i in range(len(q))):
            q.append((id, val))
        else:
            answer += 1
            if location == id:
                return answer
    