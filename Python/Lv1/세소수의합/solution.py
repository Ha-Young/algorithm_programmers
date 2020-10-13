def get_prime_list(n):
    num_list = [True] * n

    m = int(n**0.5)
    for i in range(2, m + 1):
        if num_list[i]:
            for j in range(i+i, n, i):
                num_list[j] = False

    return [i for i in range(2, n) if num_list[i]]


def solution(n):
    answer = 0

    prime_list = get_prime_list(n)
    prime_num = len(prime_list)

    for i in range(prime_num-2):
        for j in range(i+1, prime_num-1):
            for k in range(j+1, prime_num):
                if prime_list[i] + prime_list[j] + prime_list[k] == n:
                    answer += 1

    return answer
