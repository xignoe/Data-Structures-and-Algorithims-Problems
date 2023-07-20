class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squareArray = []

        for i in range(len(nums)):

            squareArray.append(nums[i] * nums[i])
            
        squareArray.sort()

        return squareArray