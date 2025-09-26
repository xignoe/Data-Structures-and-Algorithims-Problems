class Solution: 
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasingSumCount = 1 
        decreasingSumCount = 1 
        maxNum = 1
        
        for i in range(1, len(nums)): 
            if nums[i] > nums[i - 1]: 
                increasingSumCount += 1 
            else:
                increasingSumCount = 1
            if nums[i] < nums[i - 1]: 
                decreasingSumCount += 1 
            else:
                decreasingSumCount = 1
            maxNum = max(maxNum, increasingSumCount, decreasingSumCount)
        
        return maxNum