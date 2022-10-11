# 전화번호 목록
def solution(phone_book):
    answer = True
    Hash={}
    
    for key in phone_book:
        Hash[key]=1
        
    for j in phone_book:
        value=""
        for num in j:
            value += num
            if value in Hash and value !== j:
                return False
    
    return answer