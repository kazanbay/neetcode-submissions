class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1. Заранее выделяем память под массив нужной длины (хорошая практика)
        ans = [0] * (2 * n) 
        
        # 2. Бежим одним циклом по всей длине нового массива
        for i in range(2 * n):
            # Магия паттерна: индекс зацикливается благодаря % n
            ans[i] = nums[i % n] 
            
        return ans