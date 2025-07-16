class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1] * len(nums)
        productL = 1
        for i in range(len(nums)):
            answer[i] = productL
            productL *= nums[i]
        
        productR = 1
        for j in range(len(nums) - 1, -1 ,-1):
            answer[j] *= productR
            productR *= nums[j]


        return answer
