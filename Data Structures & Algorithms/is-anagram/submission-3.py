from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int) # по дефолту значение будет 0
        
        for letter in s:
            letters[letter] += 1
        for letter in t:
            letters[letter] -= 1 # вычитаем, чтобы сэкономить на втором словаре
            
        return all(count == 0 for count in letters.values())