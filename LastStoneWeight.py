class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heaviest = []
            for i in range(len(stones)):
                if len(heaviest) < 2:
                    heaviest.append(i)
                elif stones[i] >= stones[heaviest[0]] or stones[i] >= stones[heaviest[1]]:
                    if stones[heaviest[0]] > stones[heaviest[1]]:
                        heaviest[1] = i
                    else:
                        heaviest[0] = i
            heaviest.sort()
            if stones[heaviest[0]] - stones[heaviest[1]] == 0:
                stones.pop(heaviest[1])
                stones.pop(heaviest[0])
            else:
                if stones[heaviest[0]] - stones[heaviest[1]] < 0:
                    stones[heaviest[1]] -= stones[heaviest[0]]
                    stones.pop(heaviest[0])
                else:
                    stones[heaviest[0]] -= stones[heaviest[1]]
                    stones.pop(heaviest[1])

        return stones[0] if stones else 0
