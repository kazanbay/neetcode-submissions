class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        min_length = min(list(map(len, strs)))
        for i in range(min_length):
            words = [j[0:i+1] for j in strs]
            theoretical_result = words[0]
            flag = True
            for word in words[1:]:
                if theoretical_result != word:
                    flag = False
            if flag:
                result += words[0][i]
            else:
                break
        return result