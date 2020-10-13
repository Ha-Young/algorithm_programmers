from collections import deque


def solution(s):
    stack = deque([])

    for c in s:
        stack.append(c)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    if stack:
        return 0
    else:
        return 1
