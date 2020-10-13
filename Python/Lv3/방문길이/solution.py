def solution(dirs):
    answer = 0
    cur_position = [0, 0]
    visit_logs = set()

    for dir in dirs:
        cur_xpos, cur_ypos = cur_position
        # 명령어를 체크하고 다음위치를 확인한다.
        if dir == "U":
            next_position = [cur_xpos, cur_ypos + 1]
        elif dir == "L":
            next_position = [cur_xpos - 1, cur_ypos]
        elif dir == "D":
            next_position = [cur_xpos, cur_ypos - 1]
        elif dir == "R":
            next_position = [cur_xpos + 1, cur_ypos]

        # 벗어나는 영역이면 현재 위치 그대로 두고 넘어간다.
        if next_position[0] > 5 or next_position[0] < -5 or next_position[1] > 5 or next_position[1] < -5:
            continue

        # 0,0-1,0 과 같은 형태로 키를 만든다.
        visit_log = ','.join(map(str, cur_position)) + \
            '-' + ','.join(map(str, next_position))

        visit_log_reverse = ','.join(
            map(str, next_position)) + '-' + ','.join(map(str, cur_position))

        # 방문하지 않았다면 visit_logs에 방문을 기록하고 방문길이를 더한다.
        if visit_log not in visit_logs:
            answer += 1
            visit_logs.add(visit_log)
            visit_logs.add(visit_log_reverse)

        # 다음 위치로 이동한다.
        cur_position = next_position

    return answer
