class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashTable = {}

        for i in nums:
            hashTable[i] = hashTable.get(i,0) + 1

        maxHashNum = 0

        for j in hashTable:
            if hashTable[j] > maxHashNum:
                maxHashNum = hashTable[j]

        for key, value in hashTable.items():
            if value == maxHashNum:
                return(key)