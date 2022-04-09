class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        minSum = math.inf
        arrSum = 0
        
        for i in range(len(nums)):
            arrSum += nums[i]
            while arrSum >= target:
                minSum = min(minSum, i - count + 1)
                arrSum -= nums[count]
                count += 1
                
        if minSum == math.inf:
            return 0
                
        return minSum