def solution(my_string):
    answer = ''
    
    data = ['a','e','i','o','u']
    
    for i in data:
        my_string = my_string.replace(i, "")
    
    
    
    return my_string