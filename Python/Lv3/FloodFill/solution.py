from collections import deque

# 수정


def solution(n, m, image):
    answer = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = [[False]*m for _ in range(n)]

    for row in range(n):
        for col in range(m):
            if visited[row][col]:
                continue

            target_color = image[row][col]
            deq = deque([(row, col)])

            while deq:
                crow, ccol = deq.popleft()
                visited[crow][ccol] = True

                for drow, dcol in directions:
                    mrow = crow + drow
                    mcol = ccol + dcol

                    if mrow < 0 or mrow >= n or mcol < 0 or mcol >= m or visited[mrow][mcol]:
                        continue

                    if not visited[mrow][mcol] and image[mrow][mcol] == target_color:
                        deq.append((mrow, mcol))

            answer += 1

    return answer
