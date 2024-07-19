def solution(before, after):
    answer = 0
    
    before = ''.join(sorted(before))
    after = ''.join(sorted(after))

    answer =  1 if before == after else 0
    
    return answer