def solution(progresses, speeds):
    answer = []

    zip_progress_speed = [list(v) for v in zip(progresses, speeds)]

    # 작업 큐에 작업이 남아있으면 계속해서 수행
    while len(zip_progress_speed) > 0:
        # 우선 작업을 수행시킨다.
        for i in range(len(zip_progress_speed)):
            zip_progress_speed[i][0] += zip_progress_speed[i][1]

        # 앞에서 부터 작업 완료된 것이 있는지 체크한다. 완료되었으면 작업 큐에서 제거
        work_complete_num = 0
        try:
            while zip_progress_speed[0][0] >= 100:
                work_complete_num += 1
                zip_progress_speed.pop(0)
        except:  # zip_progress_speed에 아무것도 없으면 패스.
            pass

        # 완료된 작업의 개수가 0보다 크면 anwser에 추가.
        if work_complete_num > 0:
            answer.append(work_complete_num)

    return answer
