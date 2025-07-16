class Solution:
    def hammingWeight(self, n: int) -> int:
        def returnBinary(num):
            return bin(num).replace('0b', '')
        
        n = returnBinary(n)
        n = str(n)
        count = 0
        for i in range(len(n)):
            if n[i] == "1":
                count += 1
        return count