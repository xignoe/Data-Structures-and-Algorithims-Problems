class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        max1 = 0
        maxLen = 0
        windowStart = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                max1 += 1
            
            if (i - windowStart - max1 + 1) > k:
                if nums[windowStart] == 1:
                    max1 -= 1
                windowStart += 1
                
            maxLen = max(maxLen, i - windowStart + 1)
                
        return maxLen