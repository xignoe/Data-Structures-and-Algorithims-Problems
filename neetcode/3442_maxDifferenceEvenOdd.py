class Solution:
    def maxDifference(self, s: str) -> int:
        dictionary = {}

        for i in range(len(s)):
            if s[i] in dictionary:
                dictionary[s[i]] += 1
            else:
                dictionary[s[i]] = 1 

        odds = []
        evens = []

        for ch, count in dictionary.items():
            if (count % 2 == 1):
                odds.append(count)
            else:
                evens.append(count)

        maxOddCount = max(odds)
        minEvenCount = min(evens)

        return (maxOddCount - minEvenCount)

        