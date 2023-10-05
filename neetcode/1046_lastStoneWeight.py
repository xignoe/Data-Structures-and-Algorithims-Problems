class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            heaviest = stones.pop()
            heavy = stones.pop()

            if heaviest != heavy:
                diff = heaviest - heavy
                position = 0
                for i in range(len(stones)):
                    if stones[i] > diff:
                        break
                    position = i + 1
                stones.insert(position, diff)
            print(stones)  
        if stones:
            return stones[0]
        return 0