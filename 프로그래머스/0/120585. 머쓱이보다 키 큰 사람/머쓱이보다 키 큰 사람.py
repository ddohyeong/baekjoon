def solution(array, height):
    answer = 0
    
#     sorted_arr = sorted(array)
    
#     print(sorted_arr)
    
#     index = len(sorted_arr)
    
#     for i in range(len(sorted_arr)):
#         if sorted_arr[i] > height:
#             index = i
#             break
    
#     return len(sorted_arr) - index

    array.append(height)
    array.sort(reverse = True)
    return array.index(height)