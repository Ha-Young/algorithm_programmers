def solution(v):
    answer = []

    left_xpos = []
    left_ypos = []

    # Toggle 형식으로 홀수 개수인 점을 찾는다.
    for xpos, ypos in v:
        if xpos in left_xpos:
            left_xpos.remove(xpos)
        else:
            left_xpos.append(xpos)

        if ypos in left_ypos:
            left_ypos.remove(ypos)
        else:
            left_ypos.append(ypos)

    return left_xpos + left_ypos
