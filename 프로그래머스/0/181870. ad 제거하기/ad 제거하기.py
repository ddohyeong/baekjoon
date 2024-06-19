def solution(strArr):
    answer = []
    
    for arr in strArr:
        if 'ad' in arr:
            continue

        answer.append(arr)
    
    return answer