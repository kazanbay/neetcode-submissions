class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        
        # zip берет пары кортежей (char1, char2) пока оба слова не кончатся
        for char1, char2 in zip(word1, word2):
            result.append(char1)
            result.append(char2)
            
        # Магия срезов: берем длину того, что УЖЕ успели положить в result,
        # делим на 2 (так как кали в паре) — это и есть индекс конца короткого слова!
        min_len = len(result) // 2
        
        return "".join(result) + word1[min_len:] + word2[min_len:]