class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = {')': '(', '}': '{', ']': '['}
        paranthesis_order = ''
        # count_paranthesis = {'(': 0, '{': 0, '[': 0}
        flag = True
        for i in s:
            if i in ['(', '{', '[']:
                # count_paranthesis[i] += 1
                paranthesis_order += i
            if i in [')', '}', ']']:
                # count_paranthesis[paranthesis[i]] -= 1
                if paranthesis_order:
                    if paranthesis_order[-1] == paranthesis[i]:
                        paranthesis_order = paranthesis_order[:-1]
                    else:
                        flag = False
                else:
                    flag = False

            # print(paranthesis_order)
        if paranthesis_order:
            return False
        else:
            return flag