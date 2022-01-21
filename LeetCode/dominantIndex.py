class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        s = set(nums)
        
        s.remove(max(s))
        if s:  
            smax = max(s) * 2
        else:
            smax = max(nums) * 2
        for i in range(len(nums)):
            if nums[i] == max(nums) and max(nums) >= smax:
                return i
        if len(nums) == 1:
            return 0
        return -1