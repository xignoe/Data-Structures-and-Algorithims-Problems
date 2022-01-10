class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = []
        for i in range(0, m+n):
            if i < m:
                arr.append(nums1[i])
            if i >= m and i < m+n:
                arr.append(nums2[i - m])
        
        arr.sort()
        
        for l in range(len(nums1)):
            nums1[l] = arr[l]