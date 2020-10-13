import heapq


def solution(scoville, K):
    # 입력이 잘못된 경우
    if scoville == None or len(scoville) <= 0:
        return -1

    answer = 0
    heap = []

    # heap을 사용해서 자동정렬이 되도록 해준다.
    for value in scoville:
        heapq.heappush(heap, value)

    # 계속해서 mix해서 하나가 남을 때 까지 계속한다.
    while len(heap) > 1:
        # 만약, 가장 작은값이 K보다 크다면보다 큰 경우이므로 바로 answer 리턴.
        if heap[0] >= K:
            return answer

        # mix해서 다시 heap에 넣는다.
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        mixed = first + second * 2
        answer += 1
        heapq.heappush(heap, mixed)

    if len(heap) == 1 and heap[0] < K:
        return -1

    return answer
