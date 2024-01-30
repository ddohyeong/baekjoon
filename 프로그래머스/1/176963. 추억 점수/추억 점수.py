def solution(name, yearning, photo):
    answer = []
    
    for cnt in photo:
        answerNum = 0
        for i in range(len(cnt)):
            for j in range(len(name)):
                if cnt[i] == name[j]:
                    answerNum += yearning[j]
        answer.append(answerNum)
            
            
    
    return answer