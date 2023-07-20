class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        zeroCount = 0

        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[count] = nums[i]
                count += 1
            if (nums[i] == 0):
                zeroCount += 1
        
        while zeroCount > 0:
            nums[len(nums) - zeroCount] = 0
            zeroCount -= 1
