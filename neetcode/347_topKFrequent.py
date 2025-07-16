class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        mostFreq = sorted(freqMap, key=freqMap.get, reverse=True)[:k]

        return mostFreq
                


