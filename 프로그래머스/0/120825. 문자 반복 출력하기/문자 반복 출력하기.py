def solution(my_string, n):
    answer = ''
    
#     for i in my_string:
#         answer += i * n
    
    data = [i * n for i in my_string]
    print("".join(data))
    return "".join(data)