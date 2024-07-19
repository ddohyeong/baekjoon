def solution(s):
    answer = ''
    
    data = list(s)
    data.sort()
    d = ''.join(data)
    
    for i in d:
        if d.count(i) > 1:
            d = d.replace(i,'')
    
    return d