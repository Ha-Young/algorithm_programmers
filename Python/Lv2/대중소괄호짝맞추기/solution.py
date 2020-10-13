def solution(s):
    stack = []
    blanket_pairs = {'}': '{', ')': '(', ']': '['}

    for c in s:
        if c in blanket_pairs.keys():
            if stack and stack[-1] == blanket_pairs[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    if stack:
        return False

    return True
