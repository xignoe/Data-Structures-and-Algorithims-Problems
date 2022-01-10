class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        newArr = []
        for i in arr:
            newArr.append(i)
            if i == 0:
                newArr.append(i)
        
        for j in range(len(arr)):
            arr[j] = newArr[j]