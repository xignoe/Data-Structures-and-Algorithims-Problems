class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = k - 1

        mini = float("inf")

        while (r < len(nums)):
            mini = min(mini, nums[r] - nums[l])
            l += 1
            r += 1
        
        return mini