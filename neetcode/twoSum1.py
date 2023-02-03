class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}

        for i,n in enumerate(nums):
            targetNum = target - n
            if (targetNum in hashTable):
                return([i, hashTable[targetNum]])
            hashTable[n] = i