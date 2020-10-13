# 1. 일단 하나 둔다
# 2. 둔 곳에서 놓을 수 없는 곳 다 표시
# 3. 놓을 수 있는 곳에 놓는다.
# 4. 반복...



import copy

def put_queen_pos(available_chess_board, row, col, n):
    # 세로
    for drow in range(n):
        available_chess_board[drow][col] = False
    
    # 가로
    for dcol in range(n):
        available_chess_board[row][dcol] = False

    # / 대각선
    milestone = row + col
    if milestone < n:
        drow = milestone
        dcol = 0
        while drow >= 0:
            available_chess_board[drow][dcol] = False
            drow -= 1
            dcol += 1
    else:
        drow = milestone - (n - 1)
        dcol = n - 1
        while drow < n:
            available_chess_board[drow][dcol] = False
            drow += 1
            dcol -= 1

    # \ 대각선
    milestone =  row - col
    if milestone <= 0:
        drow = 0
        dcol = -milestone
        while dcol <= n - 1:
            available_chess_board[drow][dcol] = False
            drow += 1
            dcol += 1
    else:
        drow = milestone
        dcol = 0
        while drow <= n - 1:
            available_chess_board[drow][dcol] = False
            drow += 1
            dcol += 1

def get_available_n_queen(available_chess_board, history, n, history_success):
    # 종료조건 : 
    # 만약 개수가 n개면 return 1
    # 놓을곳이 없으면 return 0
    
    # 아이디어 :
    # 체스보드 받고 딥카피
    # 딥카피 한 체스보드 순회하면서 가능한 곳에 놓기
    # 반복...
    answer = 0    

    if len(history) == n:
        sort_history = tuple(sorted(history, key=lambda x: (x[0], x[1])))
        if sort_history in history_success:
            return 0
        history_success.add(sort_history)
        return 1
    
    for row in range(n):
        for col in range(n):
            if available_chess_board[row][col]:
                next_availalbe_chess_board = copy.deepcopy(available_chess_board)
                new_history = copy.deepcopy(history)
                put_queen_pos(next_availalbe_chess_board, row, col, n)
                new_history = list(new_history)
                new_history.append((row, col))
                new_history = tuple(new_history)
                answer += get_available_n_queen(next_availalbe_chess_board, new_history, n, history_success)

    return answer
    


def solution(n):
    answer = 0
    history_success = set({})
    all_available_chess_board = [[True] * n for _ in range(n)]

    answer += get_available_n_queen(all_available_chess_board, (), n, history_success)

    return answer


print(solution(4))