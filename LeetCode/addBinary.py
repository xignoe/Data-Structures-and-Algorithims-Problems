class Solution:
    def addBinary(self, a: str, b: str) -> str:
        countA, countB = 0, 0
        for i in range(len(a)):
            if (int(a[i])) == 1:
                countA += pow(2, len(a)-i)
        for i in range(len(b)):
            if (int(b[i])) == 1:
                countB += pow(2, len(b)-i)
                
        sumCount = countA + countB
        
        sumCount = bin(sumCount)[2:-1]
        if sumCount == "":
            return "0"
        
        return sumCount