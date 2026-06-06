class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = s.lower()
        palindrome = True
        was_skipped = False
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                st = s[:i]+s[i+1:]
                sl = s[:j]+s[j+1:]          
                if st == st[::-1]:
                    return True
                elif sl == sl[::-1]:
                    return True
                else:
                    return False
            else:
                j = j - 1
                i = i + 1
        return True
