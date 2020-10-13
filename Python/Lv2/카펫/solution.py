# 1. red 해서 전체 개수 구한 다음 약수 2개의 리스트를 만든다. (가로가 긴 or same)
# 2. 이 2개 약수리스트를 돌면서 가능하면 해당 크기 리턴

def get_divisor_pair(n):
    divisor_list = []
    for i in range(n, 0, -1):
        if i >= n / i and n % i == 0:
            divisor_list.append([i, int(n / i)])
    return divisor_list


def solution(brown, red):
    candidates = get_divisor_pair(red)

    for candidiate in candidates:
        red_width, red_height = candidiate
        if brown == (red_width + red_height + 2) * 2:
            return [red_width + 2, red_height + 2]

    return []
