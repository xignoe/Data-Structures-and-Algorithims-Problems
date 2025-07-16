class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap = {}
        for index, number in enumerate(nums):
            if number in hashMap:
                return number
            hashMap[number] = index