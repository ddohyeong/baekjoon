from math import gcd

def mult(array):
    c = 1
    for i in array:
        c *= i
    return c

def solution(a, b):
    answer = 0    
    
    val = gcd(a,b)
    
    tmpa = a // val
    tmpb = b // val
    
    # print(isinstance(tmpa / tmpb, int))
    if tmpa % tmpb == 0:
        return 1

    
    #소인수 분해
    b_idx = 2
    b_qnstn = []
    while tmpb > 1:
        if tmpb % b_idx == 0:
            b_qnstn.append(b_idx)
            tmpb //= b_idx
        else:
            b_idx += 1
    
    print(b_qnstn)
    
    for i in b_qnstn:
        if i != 2 and i != 5:
            return 2
        
    return 1
            
    
    
#     #소인수 분해
#     a_idx = 2
#     a_qnstn = []
#     while a > 2:
#         if a % a_idx == 0:
#             a_qnstn.append(a_idx)
#             a //= a_idx
#         else:
#             a_idx += 1
    
#     #소인수 분해
#     b_idx = 2
#     b_qnstn = []
#     while b > 2:
#         if b % b_idx == 0:
#             b_qnstn.append(b_idx)
#             b //= b_idx
#         else:
#             b_idx += 1

#     # b 소인수 중 a 중복되는 소인수를 제거
#     a_temp = a_qnstn
#     for i in a_qnstn:
#         try:
#             mm = b_qnstn.pop(b_qnstn.index(i))
#             a_temp.pop(a_temp.index(mm))
#         except: 
#             pass
    
#     aFlag, bFlag = False, False
        
    
    
#     if not 2 in b_qnstn:
#         aFlag = True
#     if not 5 in b_qnstn:
#         bFlag = True
    
#     if aFlag and bFlag:
#         return 2
#     else:
#         return 1
    
    
    