def solution(participant, completion):
    # 참여 선수 이름 배열 : participant
    # 완주 선수 이름 배열 : completion
    # 완주 못한 선수 이름 return => (참여 - 완주)
    
    #answer = ''
    Hash={}
    sumHash=0
    
    for i in participant:
        Hash[hash(i)] = i
        sumHash += hash(i)
        
    for j in completion:
        sumHash -= hash(j)
        
    return Hash[sumHash]
    
    #return answer