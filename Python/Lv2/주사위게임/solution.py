# 1-1.전체 경우의 수 구하기
# 1-2. 몬스터 만나는 경우의 수 구하기
# 2. 몬스터 만나는 확률 구하기
# 3. int(확률 * 1000)
# 최대 29 * 29 * 39 * 99 번 < 3600000

def solution(monster, S1, S2, S3):
    all_case = 0
    not_monster_case = 0
    for dice1 in range(1, S1 + 1):
        for dice2 in range(1, S2 + 1):
            for dice3 in range(1, S3 + 1):
                all_case += 1
                if 1 + dice1 + dice2 + dice3 not in monster:  # 최대 99
                    not_monster_case += 1

    not_monster_percent = not_monster_case / all_case

    return int(not_monster_percent * 1000)
