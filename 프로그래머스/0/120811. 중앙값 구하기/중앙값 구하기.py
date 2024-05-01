def solution(array):
    answer = 0
    array.sort()
    print(array[len(array)//2])
    
    return array[len(array)//2]