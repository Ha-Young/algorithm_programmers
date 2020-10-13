def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for num1, num2 in zip(A, B):
        answer += num1 * num2

    return answer
