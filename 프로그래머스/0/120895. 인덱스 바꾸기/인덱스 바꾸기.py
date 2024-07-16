def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    data1 = my_string[num1]
    data2 = my_string[num2]
    
    my_string[num2] = data1
    my_string[num1] = data2
    
    print("".join(my_string))
    
    return "".join(my_string)