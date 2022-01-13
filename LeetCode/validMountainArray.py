class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        j = len(arr) - 1
        n = len(arr)
        
        while i + 1 < n and arr[i] < arr[i + 1]: 
            i += 1
        while j > 0 and arr[j - 1] > arr[j]: 
            j -= 1
            
        return 0 < i == j < n - 1