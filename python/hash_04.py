def solution(clothes):
    Hash={}
    
    # [이름, 종류]
    for name, type in clothes:
        # get() : key로 value 얻기
        # Hash[type]로 종류 개수 가져왔음
        Hash[type] = Hash.get(type,0)+1
    
    answer = 1
    for type in Hash:
        answer*=Hash[type]
    
    
    
        
    # answer = 0
    # return answer