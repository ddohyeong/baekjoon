def solution(slice, n):
    answer = 0
    
    pizza = n // slice + (1 if n % slice else 0)
    
    return  pizza