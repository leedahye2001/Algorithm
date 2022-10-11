# 폰켓몬
def solution(nums):
    answer = 0
    n=len(nums)/2 # 최대로 가져갈 수 있는 개수
    nums=list(set(nums)) # 중복제거
    if len(nums)>=n:
        answer=n
    elif len(nums)<n:
        answer=len(nums)
    
    return answer
