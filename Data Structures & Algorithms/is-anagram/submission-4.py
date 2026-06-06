class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Базовая проверка: если длины разные, анаграмма невозможна
        if len(s) != len(t):
            return False
            
        letters = {}
        
        # 1. Наполняем словарь по строке s
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1
            
        # 2. Вычитаем по строке t
        for letter in t:
            # Если буквы из t вообще нет в словаре, или её баланс уже ушел в ноль
            if letter not in letters or letters[letter] == 0:
                return False
            letters[letter] -= 1
            
        return True