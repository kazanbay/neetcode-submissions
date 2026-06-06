class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = {')': '(', '}': '{', ']': '['}
        stack = []
        flag = True

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)

            if i in [')', '}', ']']:
                if stack:
                    if stack[-1] == paranthesis[i]:
                        stack.pop()
                    else:
                        flag = False
                else:
                    flag = False

        if stack:
            return False
        else:
            return flag