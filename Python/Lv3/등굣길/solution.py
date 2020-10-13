def solution(m, n, puddles):

    dp_paths = [[-1] * m for _ in range(n)]
    # print(dp_paths)

    for x, y in puddles:
        if x - 1 >= 0 and x - 1 < m and y - 1 >= 0 and y - 1 < n:
            dp_paths[y - 1][x - 1] = 0

    dp_paths[0][0] = 1

    print(dp_paths)

    for y in range(n):
        for x in range(m):
            if dp_paths[y][x] == 0:
                continue

            if x == 0 and y == 0:
                continue

            if y == 0 and x > 0:
                dp_paths[y][x] = dp_paths[y][x - 1]
                continue

            if x == 0 and y > 0:
                dp_paths[y][x] = dp_paths[y - 1][x]
                continue

            dp_paths[y][x] = dp_paths[y - 1][x] + dp_paths[y][x - 1]

    for row in range(n):
        print(dp_paths[row])

    return dp_paths[-1][-1] % 1000000007


print(solution(4, 3, [[2, 2]]))
