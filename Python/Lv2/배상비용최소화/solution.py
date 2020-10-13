from heapq import heapify, heappush, heappop


def solution(no, works):
    works = [x * -1 for x in works]
    heapify(works)

    for _ in range(no):
        max_work = heappop(works)  # 가장 많이 남은 작업 pop
        heappush(works, max_work + 1)  # 작업 수행 후 다시 heap에 넣는다.

    return sum(work ** 2 for work in works)


print(solution(	2, [3, 3, 3]))
