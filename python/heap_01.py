# 더 맵게
# heapq 이용

import heapq
def solution(scoville, K):
    
    heapq.heapify(scoville)
    answer=0

    while scoville[0] < K:
        mix = heapq.heappop(scoville)+(heapq.heappop(scoville)*2)
        heapq.heappush(scoville,mix)
        answer+=1
        if scoville[0] < K and len(scoville)==1:
            return -1

    return answer