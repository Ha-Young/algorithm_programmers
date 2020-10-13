def get_4operation(set1, set2):
    result_set = set([])
    for value1 in set1:
        for value2 in set2:
            result_set.add(value1 + value2)
            result_set.add(value1 - value2)
            result_set.add(value1 * value2)
            if value2 != 0:
                result_set.add(value1 // value2)

    return result_set


def solution(N, number):
    if N == number:
        return 1

    dict_dp = {}
    dict_dp[1] = set([N])
    for i in range(2, 9):
        dict_dp[i] = set([])
        for j in range(1, i):
            dict_dp[i] |= get_4operation(dict_dp[j], dict_dp[i - j])

        dict_dp[i].add(int(str(N) * i))

        if number in dict_dp[i]:
            return i

    return -1


print(solution(2, 2))
