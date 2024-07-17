def solution(numbers, direction):
    answer = []
    
    print(numbers[:len(numbers)-1])
    print([numbers[len(numbers)-1]])
    
    if direction == 'right':
        return [numbers[len(numbers)-1]] + numbers[:len(numbers)-1]
    else:
        return numbers[1:] + [numbers[0]]
    