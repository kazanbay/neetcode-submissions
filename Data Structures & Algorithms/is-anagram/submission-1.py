class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        lettert = {}
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
            # print(f'letters: {letters}')
        for letter in t:
            if letter in lettert:
                lettert[letter] += 1
            else:
                lettert[letter] = 1
            # print(f'lettert: {lettert}')
        return letters == lettert