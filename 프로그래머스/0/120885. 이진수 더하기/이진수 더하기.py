def solution(bin1, bin2):
    answer = ''
    li1sum = 0
    li1 = list(bin1)
    li1 = li1[::-1]
    li2sum = 0
    li2 = list(bin2)
    li2 = li2[::-1]
    
    for i in range(len(li1)):
        li1sum  += int(li1[i]) * (2 ** i)
    
    for i in range(len(li2)):
        li2sum  += int(li2[i]) * (2 ** i)

    print(bin(li1sum + li2sum))
    
    answer = bin(li1sum + li2sum)
        
    return answer[2:]