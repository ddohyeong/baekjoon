def solution(numbers):
    answer = 0
    
    numbers.sort(reverse = True)

    data = [numbers[0] * numbers[1],numbers[-1] * numbers[-2]]
    
    
    return max(data)