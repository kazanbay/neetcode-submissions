class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        result = ""
        # zip(*strs) берет первые буквы всех слов, потом вторые, и т.д.
        for chars in zip(*strs):
            # Если в сете один элемент — значит у всех слов на этой позиции одинаковая буква!
            if len(set(chars)) == 1:
                result += chars[0]
            else:
                break
                
        return result