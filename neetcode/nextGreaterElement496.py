class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:  
        hashTable = {}

        for i,n in enumerate(nums1):
            hashTable[n] = i

        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in hashTable:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    helper = hashTable[nums2[i]]
                    res[helper] = nums2[j]
                    break
        
        return res