class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left,right = 0, sum(nums)
        
        for i, current in enumerate(nums):
        
            right -= current

            if left == right:
                return i
            
            left += current
            
        return -1