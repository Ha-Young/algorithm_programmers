def check_bingo_horizontal(N, row, board):
    for i in range(N):
        if board[row][i] != -1:
            return False
    return True


def check_bingo_vertical(N, col, board):
    for i in range(N):
        if board[i][col] != -1:
            return False
    return True


def check_bingo_diagonal(N, board):
    for i in range(N):
        if board[i][i] != -1:
            return False
    return True


def check_bingo_diagonal_reverse(N, board):
    max_idx = N - 1
    for i in range(N):
        if board[i][max_idx - i] != -1:
            return False
    return True


def solution(board, nums):
    answer = 0

    bingo_hashboard = {}
    N = len(board)
    for row in range(N):
        for col in range(N):
            bingo_hashboard[board[row][col]] = (row, col)

    for num in nums:
        row, col = bingo_hashboard[num]

        board[row][col] = -1

        # 가로 체크
        if check_bingo_horizontal(N, row, board):
            answer += 1

        # 세로 체크
        if check_bingo_vertical(N, col, board):
            answer += 1

        # 대각선 체크 - 대각선 체크는 대각선 가능 유무도 판단한다
        if row == col and check_bingo_diagonal(N, board):
            answer += 1

        # 역 대각선 체크 - 대각선 체크는 대각선 가능 유무도 판단한다
        if row + col == N - 1 and check_bingo_diagonal_reverse(N, board):
            answer += 1

    return answer
