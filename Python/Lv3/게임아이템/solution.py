from heapq import heapify, heappush, heappop
from collections import deque


def solution(healths, items):
    answer = []
    healths.sort()
    items = deque(sorted([(item[1], item[0], idx)
                          for idx, item in enumerate(items)]))

    print(items)

    heap_items = []

    # 우선 health for문으로 시작
    for health in healths:
        if health <= 100:
            continue

        # 현재 체력에서 장착 가능한 item들을 구한다. - heap에 넣어 자동소팅되게 (어차피 가장 작은 체력 순으로 sort되어있기 때문에 다음번 health에서는 heap에 있는 item을 모두 장착 할 수 있다.)
        while items:
            debuff, buff, idx = items[0]
            if health - debuff < 100:  # 가장 작게 체력을 낮춰주는 debuff가 안되면 그 다음번것도 안될 것이니 그냥 break
                break

            items.popleft()  # heap에 넣어질 것은 pop
            heappush(heap_items, (-buff, idx))

        # 고를 수 있는 item중에서 가장 높은 공격력을 주는 item 선택
        if heap_items:
            _, idx = heappop(heap_items)
            answer.append(idx)

    return sorted(answer)


print(solution([200, 120, 150], [[30, 100], [500, 30], [100, 400]]))
