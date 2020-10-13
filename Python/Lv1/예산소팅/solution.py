def solution(d, budget):
    sum = 0
    
    d.sort()
    
    for idx, price in enumerate(d):
        sum += price
        if sum > budget:
            break
    
    if idx == len(d) - 1 and sum <= budget:
        return idx + 1
    else:
        return idx