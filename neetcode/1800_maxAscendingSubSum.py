class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += nums[i]
            else:
                current = nums[i]
            maxSum = max(maxSum, current)

        return maxSum