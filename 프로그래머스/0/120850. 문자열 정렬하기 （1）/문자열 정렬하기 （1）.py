def solution(my_string):
    answer = []
    
    answer = [int(i) for i in my_string if i.isdigit()]
    answer.sort()
    return answer