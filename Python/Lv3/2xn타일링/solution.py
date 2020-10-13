def solution(n):
    dp1 = 1
    dp2 = 2
    for i in range(2, n):
        tmp = dp2
        dp2 = dp1 + dp2
        dp1 = tmp
    
    
    return dp2 % 1000000007