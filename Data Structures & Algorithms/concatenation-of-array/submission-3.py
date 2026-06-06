class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        
        # Заполняем первую и вторую половину отдельно, без всяких %
        for i in range(n):
            ans[i] = nums[i]     # Первая половина
            ans[i + n] = nums[i] # Вторая половина (смещаемся ровно на n)
            
        return ans