class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = max(nums)
        s = set(nums)
        
        if len(s) < 3:
            return x
        
        s.remove(max(s))
        s.remove(max(s))
                
        return(max(s))