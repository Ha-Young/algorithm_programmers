def palindrom(string):
    if string == string[::-1]:
        return True
    else:
        return False


def get_substring_combination(origin_string, hope_length):
    result_arr = []

    for i in range(len(origin_string) - (hope_length - 1)):
        sub_string = origin_string[i:i + hope_length]
        result_arr.append(sub_string)

    return result_arr


def solution(s):
    answer = 0
    s_length = len(s)

    while s_length > 0:
        if s_length % 2 == 1:
            sub_s = get_substring_combination(s, s_length)

            for sub in sub_s:
                if palindrom(sub):
                    return len(sub)

        s_length -= 1

    return answer


print(solution("abcdcba"))
