class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        hashTable = {}

        for i,n in enumerate(set(text)):
            hashTable[n] = 0

        for j in range(len(text)):
            if text[j] in hashTable:
                hashTable[text[j]] += 1

        count = 0
        ballArr = []
        b = hashTable.get('b')
        a = hashTable.get('a')
        l = hashTable.get('l')
        o = hashTable.get('o')
        n = hashTable.get('n')
        ballArr.append(b)
        ballArr.append(a)
        ballArr.append(l)
        ballArr.append(o)
        ballArr.append(n)

        for i in range(len(text)):
            if(ballArr[0] >= 1 and ballArr[1] >= 1 and ballArr[2] >= 2 and ballArr[3] >= 2 and ballArr[4] >= 1):
                ballArr[0] -= 1
                ballArr[1] -= 1
                ballArr[2] -= 2
                ballArr[3] -= 2
                ballArr[4] -= 1
                count += 1

        return count