class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        sumD = 0
        sumND = 0
        matMax = len(mat)
        matMaxCount = len(mat)

        while count < matMax:
            sumD += mat[count][count]
            sumND += mat[count][matMaxCount - 1]
            count += 1
            matMaxCount -= 1
        
        totalSum = sumD + sumND
        
        if len(mat) % 2 == 1:
            totalSum -= mat[len(mat) // 2][len(mat) // 2]

        return totalSum