class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1,0, -1):
            if arr[i] >= arr[i-1]:
                arr[i-1] = arr[i]
        arr.append(-1)
        return arr[1:]