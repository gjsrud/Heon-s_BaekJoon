#힙
#가장안매운거 + (두번째로 안매운거*2)

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:


        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        if a >= K:
            break
        
        answer += 1

        heapq.heappush(scoville, a+(b*2))

        #print(scoville)

        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        if len(scoville) == 1 and scoville[0] > K:
            return answer

    return answer

print(solution([1, 2, 3],11))
        
'''

'''