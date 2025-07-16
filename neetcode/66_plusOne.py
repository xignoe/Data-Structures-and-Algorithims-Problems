class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strNum = ""
        strArr = []
        for i in range(len(digits)):
            strNum += (str(digits[i]))

        strNum = int(strNum) + 1
        
        strNum = str(strNum)
    
        for j in range(len(strNum)):
            strArr.append(strNum[j])

        for k in range(len(strArr)):
            strArr[k] = int(strArr[k])

        return strArr