def rotate90(origin_arr):
    M = len(origin_arr)
    rotate_arr = [[0]*M for _ in range(M)]

    for row in range(M):
        for col in range(M):
            rotate_arr[col][M-1-row] = origin_arr[row][col]

    return rotate_arr


def move_right(origin_arr):
    M = len(origin_arr)
    move_arr = [[0]*M for _ in range(M)]

    for row in range(M):
        for col in range(M - 1):
            move_arr[row][col+1] = origin_arr[row][col]

    return move_arr


def move_left(origin_arr):
    M = len(origin_arr)
    move_arr = [[0]*M for _ in range(M)]

    for row in range(M):
        for col in range(1, M):
            move_arr[row][col-1] = origin_arr[row][col]

    return move_arr


def move_up(origin_arr):
    M = len(origin_arr)
    move_arr = [[0]*M for _ in range(M)]

    for row in range(1, M):
        for col in range(M):
            move_arr[row - 1][col] = origin_arr[row][col]

    return move_arr


def move_down(origin_arr):
    M = len(origin_arr)
    move_arr = [[0]*M for _ in range(M)]

    for row in range(M - 1):
        for col in range(M):
            move_arr[row + 1][col] = origin_arr[row][col]

    return move_arr


def isMatch(key, lock):
    M = len(key)
    if M != len(lock):
        raise Exception('key와 lock의 크기가 맞지 않습니다.')

    for row in range(M):
        for col in range(M):
            if key[row][col] + lock[row][col] != 1:
                return False

    return True


def size_up(origin_key, N):
    M = len(origin_key)
    new_key = [[0]*N for _ in range(N)]

    for row in range(M):
        for col in range(M):
            new_key[row][col] = origin_key[row][col]

    return new_key


def check_all_zero(key):
    M = len(key)
    for row in range(M):
        for col in range(M):
            if key[row][col] != 0:
                return False

    return True


def solution(key, lock):
    # key를 lock 사이즈에 맞게 변경
    M = len(key)
    N = len(lock)
    if M < N:
        key = size_up(key, N)
    stack = [key]

    checked_key = set({})

    # DFS 이용할 것임
    while stack:
        cur_key = stack.pop()
        checked_key_key = tuple(map(tuple, cur_key))
        if checked_key_key in checked_key or check_all_zero(cur_key):
            continue
        checked_key.add(checked_key_key)

        # 90도 회전
        new_key = rotate90(cur_key)
        if isMatch(new_key, lock):
            return True
        stack.append(new_key)

        # 오른쪽 이동
        new_key = move_right(cur_key)
        if isMatch(new_key, lock):
            return True
        stack.append(new_key)

        # 왼쪽 이동
        new_key = move_left(cur_key)
        if isMatch(new_key, lock):
            return True
        stack.append(new_key)

        # 아래 이동
        new_key = move_down(cur_key)
        if isMatch(new_key, lock):
            return True
        stack.append(new_key)

        # 위 이동
        new_key = move_up(cur_key)
        if isMatch(new_key, lock):
            return True
        stack.append(new_key)

    # 모든 경우의 수 안되면 False
    return False


print(solution([[1, 1, 1, 1], [1, 0, 0, 1], [0, 1, 1, 1], [0, 0, 0, 1]],
               [[1, 1, 1, 1, 0], [1, 1, 0, 0, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 0]]))
