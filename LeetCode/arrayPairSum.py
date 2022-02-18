class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sumNum = 0
        
        for i in range(0 ,len(nums) , 2):
            sumNum += nums[i]
        
        return sumNum