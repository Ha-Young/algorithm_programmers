# def get_words_nth(strs, t, dp, nth):
#     ret_nth_words = set({})

#     if nth == 1:
#         for str_ in strs:
#             if len(t) >= len(str_) and t[0:len(str_)] == str_:
#                 ret_nth_words.add(str_)
#     else:
#         prev_words = dp[nth - 1]

#         for prev_word in prev_words:
#             for str_ in strs:
#                 new_word = prev_word + str_

#                 if len(t) >= len(new_word) and t[0:len(new_word)] == new_word:
#                     ret_nth_words.add(prev_word + str_)

#     return ret_nth_words


# def solution(strs, t):
#     count = 0

#     # 1. dir > set
#     dp = dict({})

#     # 2. count가 목표 문자열의 길이보다 커지면 종료. strs에서 가장 작은 길이가 1이므로.
#     while count <= len(t):
#         count += 1
#         dp[count] = get_words_nth(strs, t, dp, count)

#         if t in dp[count]:
#             return count

#     return -1


def solution(strs, t):
    dp = [0] * (len(t) + 1)

    strs = set(strs)

    for i in range(1, len(t) + 1):
        dp[i] = float('inf')
        for j in range(1, 6):
            start = i - j
            end = i
            if start >= 0 and t[start:end] in strs:
                dp[i] = min(dp[i], dp[i - j] + 1)

    return -1 if dp[-1] == float('inf') else dp[-1]


print(solution(	["ab", "na", "n", "a", "bn"], "nabnabn"))
