class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = filter(lambda x: x.isalnum(), s.lower())
        s2 = "".join(s1)
        return s2 == s2[::-1]