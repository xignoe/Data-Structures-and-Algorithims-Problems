class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setNum = set(nums)
        resultArr = []
        orderedNums = []
        for i in range(1, len(nums) + 1):
            orderedNums.append(i)
        
        for j in range(len(nums)):
            if orderedNums[j] not in setNum:
                resultArr.append(j + 1)

        return resultArr