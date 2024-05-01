from collections import Counter


def solution(array):
    answer = 0
    
    counter = Counter(array)
        
    s = sorted(dict(counter).items(),key = lambda x : x[1])
    

    print(s)
    if len(s) == 1:
        return s[0][0]
    elif len(s) > 1 and s[-1][1] == s[-2][1]:
        return -1
    elif len(s) > 1 and s[-1][1] != s[-2][1]:
        return s[-1][0]