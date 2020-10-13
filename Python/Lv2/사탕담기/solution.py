from itertools import combinations


def solution(m, weights):
    answer = 0
    all_case = []

    for i in range(1, len(weights) + 1):
        all_case.extend(list(combinations(weights, i)))

    for case in all_case:
        if sum(case) == m:
            answer += 1

    return answer
